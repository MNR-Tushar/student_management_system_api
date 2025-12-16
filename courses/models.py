from django.db import models
from departments.models import Department
class Course(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=30,unique=True)
    credit=models.DecimalField(max_digits=6,decimal_places=2)
    semester=models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.title
