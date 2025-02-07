from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    student_number = models.IntegerField()
    

class Department(models.Model):
    name  = models.CharField(max_length=20)
    administrator  = models.CharField(max_length=20)

class Issue(models.Model):
    sender = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    summary = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    attachments = models.FileField()