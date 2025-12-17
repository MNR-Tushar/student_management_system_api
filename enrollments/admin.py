from django.contrib import admin
from .models import Enrollment
@admin.register(Enrollment)
class enrollmentsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id', 'enrollment_date')
    search_fields = ('student_id', 'course_id', 'enrollment_date')
