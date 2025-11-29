from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class DepartmentViewset(viewsets.GenericViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    pagination_class = LimitOffsetPagination
    def list(self, request):
        departments=self.get_queryset()
        page = self.paginate_queryset(departments)
        serializer=self.get_serializer(page,many=True)
        return self.get_paginated_response(serializer.data)
    
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

class StudentsViewset(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['name','student_id','email','phone','address','gender','dob','admission_date']
    ordering_fields=['name']
    filterset_fields = {
        'department': ['exact','in'],
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
        
        

class TeachersViewset(viewsets.GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    pagination_class = LimitOffsetPagination

    def list(self,request):
        teacher=self.get_queryset()
        page=self.paginate_queryset(teacher)
        serializer=self.get_serializer(page,many=True)
        return self.get_paginated_response(serializer.data)
    
    def create(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, pk=None):
        teacher=self.get_object()
        serializer=self.get_serializer(teacher,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self,request,pk=None):
        teacher=self.get_object()
        teacher.delete()
        return Respone(status=2024)
    
    def retrieve(self,request,pk=None):
        teacher=self.get_object()
        serializer=self.get_serializer(teacher)
        return Response(serializer.data)
        

class CoursesViewset(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    pagination_class = LimitOffsetPagination
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
        course.detele()
        return Response(status=204)
    
    def retrieve(self,request,pk=None):
        course=self.get_object()
        serializer=self.get_serializer(course)
        return Response(serializer.data)


class EnrollmentsViewset(viewsets.GenericViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields=['student__id','course__id','enrollment_date']
    ordering_fields=['enrollment_date','student__id','course__id']
    filterset_fields = {
        'student': ['exact','in'],
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



