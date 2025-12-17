from django.contrib import admin
from .models import Teacher
@admin.register(Teacher)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher_id', 'designation', 'email', 'phone', 'address', 'department')
    search_fields = ('name', 'teacher_id', 'designation', 'email', 'phone', 'address', 'department')
