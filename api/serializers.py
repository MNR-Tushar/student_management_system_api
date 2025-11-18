from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        models =Department
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        models =Students
        fields = '__all__'

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        models =Teachers
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        models =Courses
        fields = '__all__'

class enrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        models =enrollments
        fields = '__all__'