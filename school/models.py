from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    email = models.EmailField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    parent_guardian_name = models.CharField(max_length=100, blank=True)
    parent_guardian_phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='students/profile_pictures/')
    
    def __str__(self):
        return self.user.username


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='staff/profile_pictures/')
    
    def __str__(self):
        return self.user.username


class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    attachments = models.FileField(upload_to='activities/attachments/')
    
    def __str__(self):
        return self.title


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.PositiveIntegerField()
    document = models.FileField(upload_to='results/documents/', null= True)  
    
    def __str__(self):
        return f"{self.student.user.username}'s {self.subject} Result"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title