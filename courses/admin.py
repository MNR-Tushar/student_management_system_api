from django.contrib import admin
from .models import *
@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'credit', 'semester', 'department')
    search_fields = ('title', 'code', 'credit', 'semester', 'department')
