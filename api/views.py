from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated



class StudentsViewset(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['name','student_id','email','phone','address','gender','dob','admission_date','department__name']
    ordering_fields=['name']
    filterset_fields = {
        'department': ['exact','in'],
        'department__name': ['exact'],
        'gender': ['exact'],
    }

    def list(self,request):
        student=self.get_queryset()
        filter_queryset=self.filter_queryset(student)
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
    
    def partial_update(self, request,pk=None):
        student=self.get_object()
        serializer=self.get_serializer(student,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self,request,pk=None):
        student=self.get_object()
        student.delete()
        return Response(status=204)
    
    def retrieve(self,request,pk=None):
        student=self.get_object()
        serializer=self.get_serializer(student)
        return Response(serializer.data)
        
        




class EnrollmentsViewset(viewsets.GenericViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['student__name','course__title','enrollment_date']
    ordering_fields=['enrollment_date','student__name','course__title']
    filterset_fields = {
        'student': ['exact','in'],
        'course': ['exact','in'],
        'course__title': ['exact'],
    }

    def list(self,request):
        enrollments=self.get_queryset()
        filter_queryset=self.filter_queryset(enrollments)
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
        enrollments=self.get_object()
        serializer=self.get_serializer(enrollments,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self,request,pk=None):
        enrollments=self.get_object()
        enrollments.delete()
        return Response(status=204)
    
    def retrieve(self,request,pk=None):
        enrollments=self.get_object()
        serializer=self.get_serializer(enrollments)
        return Response(serializer.data)