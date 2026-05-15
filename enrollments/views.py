from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache


ENROLLMENT_LIST_KEY   = 'enrollment_list'
ENROLLMENT_DETAIL_KEY = 'enrollment_detail_{pk}'
CACHE_TTL             = 60 * 10  # 10 minutes (enrollment বেশি change হয়)


class EnrollmentsViewset(viewsets.GenericViewSet):
    queryset = Enrollment.objects.select_related('student', 'course').all()
    serializer_class = EnrollmentsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['student__name', 'course__title', 'enrollment_date']
    ordering_fields = ['enrollment_date', 'student__name', 'course__title']
    filterset_fields = {
        'student': ['exact', 'in'],
        'course': ['exact', 'in'],
        'course__title': ['exact'],
    }

    # ── READ ──────────────────────────────────────────────────────────────────

    def list(self, request):
        cache_key = f"{ENROLLMENT_LIST_KEY}_{request.query_params.urlencode()}"
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
        cache_key = ENROLLMENT_DETAIL_KEY.format(pk=pk)
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        enrollment = self.get_object()
        serializer = self.get_serializer(enrollment)
        cache.set(cache_key, serializer.data, CACHE_TTL)
        return Response(serializer.data)

    # ── WRITE ─────────────────────────────────────────────────────────────────

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete_pattern(f"{ENROLLMENT_LIST_KEY}_*")
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        enrollment = self.get_object()
        serializer = self.get_serializer(enrollment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete(ENROLLMENT_DETAIL_KEY.format(pk=pk))
        cache.delete_pattern(f"{ENROLLMENT_LIST_KEY}_*")
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        enrollment = self.get_object()
        enrollment.delete()
        cache.delete(ENROLLMENT_DETAIL_KEY.format(pk=pk))
        cache.delete_pattern(f"{ENROLLMENT_LIST_KEY}_*")
        return Response(status=204)