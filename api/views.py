from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache


STUDENT_LIST_KEY   = 'student_list'
STUDENT_DETAIL_KEY = 'student_detail_{pk}'
CACHE_TTL          = 60 * 15  # 15 minutes


class StudentsViewset(viewsets.GenericViewSet):
    queryset = Student.objects.select_related('department').all()
    serializer_class = StudentsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'student_id', 'email', 'phone', 'address',
                     'gender', 'dob', 'admission_date', 'department__name']
    ordering_fields = ['name']
    filterset_fields = {
        'department': ['exact', 'in'],
        'department__name': ['exact'],
        'gender': ['exact'],
    }

    # ── READ ──────────────────────────────────────────────────────────────────

    def list(self, request):
        cache_key = f"{STUDENT_LIST_KEY}_{request.query_params.urlencode()}"
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        qs = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data).data
            cache.set(cache_key, result, CACHE_TTL)
            return Response(result)

        serializer = self.get_serializer(qs, many=True)
        cache.set(cache_key, serializer.data, CACHE_TTL)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        cache_key = STUDENT_DETAIL_KEY.format(pk=pk)
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        student = self.get_object()
        serializer = self.get_serializer(student)
        cache.set(cache_key, serializer.data, CACHE_TTL)
        return Response(serializer.data)

    # ── WRITE ─────────────────────────────────────────────────────────────────

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete_pattern(f"{STUDENT_LIST_KEY}_*")
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete(STUDENT_DETAIL_KEY.format(pk=pk))
        cache.delete_pattern(f"{STUDENT_LIST_KEY}_*")
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        student = self.get_object()
        student.delete()
        cache.delete(STUDENT_DETAIL_KEY.format(pk=pk))
        cache.delete_pattern(f"{STUDENT_LIST_KEY}_*")
        return Response(status=204)