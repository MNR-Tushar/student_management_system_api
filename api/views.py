from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

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



