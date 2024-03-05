# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User



class Feedback(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField(max_length=50)
    Door_Number = models.CharField(max_length=10) 
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name, f"Feedback #{self.id}"

class Carpenter(models.Model):
    name = models.CharField(max_length=100)
    exp = models.IntegerField()
    skills = models.TextField()
    dob = models.DateField()
    address = models.TextField()
    number = models.CharField(max_length=15)
    completed_projects = models.IntegerField()
    
class Inquiry(models.Model):
    room_dimensions = models.CharField(max_length=255)
    bed_type = models.CharField(max_length=50)
    color_preference = models.CharField(max_length=255)
    budget = models.CharField(max_length=50)
    room_layout = models.TextField()
    comments = models.TextField()
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    wardrobe_size = models.CharField(max_length=255)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    uniform_cleanliness = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)



class Reply(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    




