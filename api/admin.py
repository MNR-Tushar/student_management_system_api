from django.contrib import admin
from .models import *

@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'email', 'phone', 'address', 'gender', 'dob', 'admission_date', 'department')
    search_fields = ('name', 'student_id', 'email', 'phone', 'address', 'gender', 'dob', 'admission_date', 'department')

@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher_id', 'designation', 'email', 'phone', 'address', 'department')
    search_fields = ('name', 'teacher_id', 'designation', 'email', 'phone', 'address', 'department')


@admin.register(Enrollment)
class enrollmentsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id', 'enrollment_date')
    search_fields = ('student_id', 'course_id', 'enrollment_date')