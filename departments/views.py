from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache


DEPT_LIST_KEY   = 'department_list'
DEPT_DETAIL_KEY = 'department_detail_{pk}'
CACHE_TTL       = 60 * 15  # 15 minutes


class DepartmentViewset(viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'code']
    filterset_fields = {
        'name': ['exact', 'in'],
        'code': ['exact'],
    }

    # ── READ ──────────────────────────────────────────────────────────────────

    def list(self, request):
        # query params আলাদা হলে আলাদা cache key — filter/search সব কাজ করবে
        cache_key = f"{DEPT_LIST_KEY}_{request.query_params.urlencode()}"
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
        cache_key = DEPT_DETAIL_KEY.format(pk=pk)
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        department = self.get_object()
        serializer = self.get_serializer(department)
        cache.set(cache_key, serializer.data, CACHE_TTL)
        return Response(serializer.data)

    # ── WRITE (cache invalidate করে) ─────────────────────────────────────────

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete_pattern(f"{DEPT_LIST_KEY}_*")
        return Response(serializer.data)

    def update(self, request, pk=None):
        department = self.get_object()
        serializer = self.get_serializer(department, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete(DEPT_DETAIL_KEY.format(pk=pk))
        cache.delete_pattern(f"{DEPT_LIST_KEY}_*")
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        department = self.get_object()
        serializer = self.get_serializer(department, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete(DEPT_DETAIL_KEY.format(pk=pk))
        cache.delete_pattern(f"{DEPT_LIST_KEY}_*")
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        department = self.get_object()
        department.delete()
        cache.delete(DEPT_DETAIL_KEY.format(pk=pk))
        cache.delete_pattern(f"{DEPT_LIST_KEY}_*")
        return Response(status=204)