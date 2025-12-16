from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class CoursesViewset(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['title','code','credit','semester','department__name']
    ordering_fields=['title','code']
    filterset_fields = {
        'department__name': ['exact'],
        'semester': ['exact'],
    }

    def list(self,request):
        course=self.get_queryset()
        filter_queryset=self.filter_queryset(course)
        page=self.paginate_queryset(filter_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer=self.get_serializer(filter_queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self,request,pk=None):
        course=self.get_object()
        serializer=self.get_serializer(course,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    def update(self,request,pk=None):
        course=self.get_object()
        serializer=self.get_serializer(course,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self,request,pk=None):
        course=self.get_object()
        course.delete()  # Fixed: was detele()
        return Response(status=204)
    
    def retrieve(self,request,pk=None):
        course=self.get_object()
        serializer=self.get_serializer(course)
        return Response(serializer.data)