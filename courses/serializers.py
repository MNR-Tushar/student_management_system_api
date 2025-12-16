from rest_framework import serializers
from courses.models import *
class CoursesSerializer(serializers.ModelSerializer):
    department_name=serializers.ReadOnlyField(source='department.name')
    class Meta:
        model = Course
        fields = ['id','title','code','credit','semester','department','department_name']