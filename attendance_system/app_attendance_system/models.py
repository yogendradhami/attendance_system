from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = {
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    }

    user_type= models.CharField(choices=USER, max_length=1, default=1)
    profile_pic = models.ImageField(upload_to='static/assets/img/profile_pic/')


class Cource(models.Model):
    name= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Session_Year(models.Model):
    session_start= models.CharField(max_length=100)
    session_end= models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " to " + self.session_end

class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    gender=models.CharField( max_length=50)
    cource_id = models.ForeignKey(Cource, on_delete=models.DO_NOTHING)
    session_year_id= models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    

class Staff(models.Model):
    admin=  models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.admin.username

class Subject(models.Model):
    name=models.CharField(max_length=100)
    cource=models.ForeignKey(Cource, on_delete=models.CASCADE)
    staff= models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Staff_Notification(models.Model):
    staff_id= models.ForeignKey(Staff,on_delete=models.CASCADE)
    message=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.staff_id.admin.first_name + ' ' + self.staff_id.admin.last_name
    
class Staff_Leave(models.Model):
    staff_id= models.ForeignKey(Staff, on_delete=models.CASCADE)
    date= models.CharField(max_length=100)
    message= models.TextField()
    status=models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff_id.admin.first_name + ' ' + self.staff_id.admin.last_name

class Staff_feedback(models.Model):
    staff_id= models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback= models.TextField()
    feedback_reply=models.TextField()
    status=models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + ' ' + self.staff_id.admin.last_name  
    

# models for student
class Student_Notification(models.Model):
    student_id= models.ForeignKey(Student,on_delete=models.CASCADE)
    message=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(null=True,default=0)
    
    def __str__(self):
        return self.student_id.admin.first_name + ' ' + self.student_id.admin.last_name
    
class Student_Feedback(models.Model):
    student_id= models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback= models.TextField()
    feedback_reply=models.TextField()
    status=models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + ' ' + self.student_id.admin.last_name 
    
class Student_Leave(models.Model):
    student_id= models.ForeignKey(Student, on_delete=models.CASCADE)
    date= models.CharField(max_length=100)
    message= models.TextField()
    status=models.IntegerField(default=0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name + ' ' + self.student_id.admin.last_name