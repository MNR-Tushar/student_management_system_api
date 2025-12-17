from django.db import models
from api.models import Student
from courses.models import Course
class Enrollment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    enrollment_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

