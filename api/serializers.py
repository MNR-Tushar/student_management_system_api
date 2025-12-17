from rest_framework import serializers
from .models import *
from courses.serializers import CoursesSerializer
from departments.serializers import DepartmentSerializer
from departments.models import Department
class StudentsSerializer(serializers.ModelSerializer):
    department_name=serializers.ReadOnlyField(source='department.name',read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','email','phone','department','department_name','student_id','address','gender','dob','admission_date']





