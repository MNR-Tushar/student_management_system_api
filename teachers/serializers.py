
from rest_framework import serializers
from .models import *
from courses.serializers import CoursesSerializer

class TeachersSerializer(serializers.ModelSerializer):
    department_name=serializers.ReadOnlyField(source='department.name',read_only=True)
    class Meta:
        model = Teacher
        fields = ['id','name','teacher_id','designation','email','phone','address','department','department_name']