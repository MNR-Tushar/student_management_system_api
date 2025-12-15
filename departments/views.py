from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class DepartmentViewset(viewsets.GenericViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['name','code']
    ordering_fields=['name','code']
    
    filterset_fields = {
        'name': ['exact','in'],
        'code': ['exact'],
    }
    
    
    
    def list(self, request):
        department=self.get_queryset()
        filter_queryset=self.filter_queryset(department)
        page = self.paginate_queryset(filter_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer=self.get_serializer(filter_queryset,many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        department=self.get_object()
        serializer=self.get_serializer(department,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        department=self.get_object()
        serializer=self.get_serializer(department,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        department=self.get_object()
        department.delete()
        return Response(status=204)
    
    def retrieve(self, request, pk=None):
        department=self.get_object()
        serializer=self.get_serializer(department)
        return Response(serializer.data)
