from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=20)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class Students(models.Model):
    gender_choices=(('male','Male'),('female','Female'))

    name=models.CharField(max_length=100)
    student_id=models.CharField(max_length=30,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=10,choices=gender_choices)
    dob=models.DateField(null=True,blank=True)
    admission_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Teachers(models.Model):
    name=models.CharField(max_length=100)
    teacher_id=models.CharField(max_length=30,unique=True)
    designation=models.CharField(max_length=100)
    email=models.EmailField(max_length=50,unique=True)
    phone=models.CharField(max_length=20,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=30,unique=True)
    credit=models.DecimalField(max_digits=6,decimal_places=2)
    semester=models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class enrollments(models.Model):
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE,null=True,blank=True)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True,blank=True)
    enrollment_date=models.DateField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

   

