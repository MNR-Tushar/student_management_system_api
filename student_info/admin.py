from django.contrib import admin
from .models import *

@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'email', 'phone', 'address', 'gender', 'dob', 'admission_date', 'department')
    search_fields = ('name', 'student_id', 'email', 'phone', 'address', 'gender', 'dob', 'admission_date', 'department')




