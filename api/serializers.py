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

class EnrollmentsSerializer(serializers.ModelSerializer):

    student_name=serializers.CharField(write_only=True,required=True)
    course_name=serializers.CharField(write_only=True,required=True)

    student=StudentsSerializer(read_only=True)
    course=CoursesSerializer(read_only=True)

    class Meta:
        model =Enrollments
        fields='__all__'
        
    #     fields = ['id','course_name','student_name','enrollment_date','created_at','updated_at','student','course']


    # def create(self,validated_data):
    #     student_name=self.validated.data.pop('student_name')
    #     course_name=self.validated.data.pop('course_name')

    #     student=Students.objects.get(name=student_name)
    #     course=Courses.objects.get(title=course_name)

    #     return Enrollments.objects.create(student=student,course=course,**validated_data)

    # def update(self, instance, validated_data):
    #     if 'student_name' in validated_data:
    #         student = Students.objects.get(name=validated_data.pop('student_name'))
    #         instance.student = student

    #     if 'course_name' in validated_data:
    #         course = Courses.objects.get(name=validated_data.pop('course_name'))
    #         instance.course = course

    #     return super().update(instance, validated_data)    