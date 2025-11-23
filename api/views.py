from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
class DepartmentViewset(viewsets.GenericViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
    def list(self, request):
        departments=self.get_queryset()
        serializer=self.get_serializer(departments,many=True)
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

class StudentsViewset(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    def list(self,request):
        student=self.get_queryset()
        serializer=self.get_serializer(student,many=True)
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
    
    def destory(self,request,pk=None):
        student=self.get_object()
        student.delete()
        return Response(status=204)
    
    def retrieve(self,request,pk=None):
        student=self.get_object()
        serializer=self.get_serializer(student)
        return Response(serializer.data)
        
        

class TeachersViewset(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer

    def list(self,request):
        teacher=self.get_queryset()
        serializer=self.get_serializer(teacher,many=True)
        return Response(serializer.data)
    
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
    
    def destory(self,request,pk=None):
        teacher=self.get_object()
        teacher.delete()
        return Respone(status=2024)
    
    def retrieve(self,request,pk=None):
        teacher=self.get_object()
        serializer=self.get_serializer(teacher)
        return Response(serializer.data)
        

class CoursesViewset(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    def list(self,request):
        course=self.get_queryset()
        serializer=self.get_serializer(course,many=True)
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
    
    def destory(self,request,pk=None):
        course=self.get_object()
        course.detele()
        return Response(status=204)
    
    def retrieve(self,request,pk=None):
        course=self.get_object()
        serializer=self.get_serializer(course)
        return Response(serializer.data)


class EnrollmentsViewset(viewsets.ModelViewSet):
    queryset = enrollments.objects.all()
    serializer_class = enrollmentsSerializer

    def list(self,request):
        enrollments=self.get_queryset()
        serializer=self.get_serializer(enrollments,many=True)
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
    
    def destory(self,request,pk=None):
        enrollments=self.get_object()
        enrollments.delete()
        return Response(status=204)
    
    def retrieve(self,request,pk=None):
        enrollments=self.get_object()
        serializer=self.get_serializer(enrollments)
        return Response(serializer.data)



