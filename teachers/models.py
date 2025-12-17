from django.db import models
from departments.models import Department
class Teacher(models.Model):
    name=models.CharField(max_length=100)
    teacher_id=models.CharField(max_length=30,unique=True)
    designation=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        
        return self.name



