from rest_framework import serializers
from .models import *
from courses.serializers import CoursesSerializer

class StudentsSerializer(serializers.ModelSerializer):
    department_name=serializers.ReadOnlyField(source='department.name',read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','email','phone','department','department_name','student_id','address','gender','dob','admission_date']





class EnrollmentsSerializer(serializers.ModelSerializer):
    student_name=serializers.CharField(write_only=True,required=False)
    course_name=serializers.CharField(write_only=True,required=False)

    student_detail=StudentsSerializer(source='student', read_only=True)
    course_detail=CoursesSerializer(source='course', read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id','student','course','student_name','course_name','student_detail','course_detail','enrollment_date','created_at']

    def create(self, validated_data):
        # Remove write-only fields before creating
        validated_data.pop('student_name', None)
        validated_data.pop('course_name', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Remove write-only fields before updating
        validated_data.pop('student_name', None)
        validated_data.pop('course_name', None)
        return super().update(instance, validated_data)