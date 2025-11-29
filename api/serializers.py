from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Department
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    department_name=serializers.ReadOnlyField(source='department.name',read_only=True)
    class Meta:
        model =Student
        fields = ['name','email','phone','department','department_name','student_id','address','gender','dob','admission_date']

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
        
    