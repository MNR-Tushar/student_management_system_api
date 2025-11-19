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

class TeachersViewset(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer


class CoursesViewset(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class EnrollmentsViewset(viewsets.ModelViewSet):
    queryset = enrollments.objects.all()
    serializer_class = enrollmentsSerializer



