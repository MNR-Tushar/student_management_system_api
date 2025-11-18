from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Department
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Students
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model =Teachers
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Courses
        fields = '__all__'

class enrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model =enrollments
        fields = '__all__'