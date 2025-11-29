from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Department
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model =Teacher
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    department_name=serializers.ReadOnlyField(source='department.name')
    class Meta:
        model =Course
        fields = ['title','code','credit','semester','department','department_name']

class EnrollmentsSerializer(serializers.ModelSerializer):

    student_name=serializers.CharField(write_only=True,required=True)
    course_name=serializers.CharField(write_only=True,required=True)

    student=StudentsSerializer(read_only=True)
    course=CoursesSerializer(read_only=True)

    class Meta:
        model =Enrollment
        fields='__all__'
        
    