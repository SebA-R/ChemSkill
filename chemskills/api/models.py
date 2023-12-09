from django.db import models
import os

def generate_unique_code():
    length = 4
    while True:
        code = os.urandom(length).hex().upper()
        if Classroom.objects.filter(code=code).count() == 0:
            return code
    

# Create your models here.
class Classroom(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    name = models.CharField(max_length=32, default="")
    teachers = models.CharField(max_length=320, default="")
    students = models.CharField(max_length=640, default="")
    created_at = models.DateTimeField(auto_now_add=True)
