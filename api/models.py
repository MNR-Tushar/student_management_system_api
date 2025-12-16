from django.db import models
from departments.models import Department
from courses.models import Course
class Student(models.Model):
    gender_choices=(('male','Male'),('female','Female'))

    name=models.CharField(max_length=100)
    student_id=models.CharField(max_length=30,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=10,choices=gender_choices)
    dob=models.DateField(null=True,blank=True)
    admission_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
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




class Enrollment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    enrollment_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)

   

