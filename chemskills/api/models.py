from django.db import models
import os

def generate_unique_code():
    length = 4
    while True:
        code = os.urandom(length).hex().upper()
        if Classroom.objects.filter(code=code).count() == 0:
            return code
    
class User(models.Model):
    username = models.CharField(max_length=32, default="", unique=True)
    password = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=64, default="")
    first_name = models.CharField(max_length=32, default="")
    last_name = models.CharField(max_length=32, default="")
    is_teacher = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    classrooms = models.CharField(max_length=640, default="", null=True)
    current_chapter = models.CharField(max_length=32, default="", null=True)

class Classroom(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    name = models.CharField(max_length=32, default="")
    teachers = models.CharField(max_length=320, default="")
    students = models.CharField(max_length=640, default="")
    created_at = models.DateTimeField(auto_now_add=True)
