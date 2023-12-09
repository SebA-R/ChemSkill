from rest_framework import serializers
from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'code', 'name', 'teachers', 'students', 'created_at')

class CreateClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('name', 'teachers', 'students')