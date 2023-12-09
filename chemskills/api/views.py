from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import ClassroomSerializer, CreateClassroomSerializer, UserSerializer
from .models import Classroom, User
from rest_framework.views import APIView
from rest_framework.response import Response
import json


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

class ClassroomView(generics.ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class CreateClassroomView(APIView):
    serializer_class = CreateClassroomSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            teachers = serializer.data.get("teachers")
            name = serializer.data.get("name")
            classroom = Classroom(name=name, teachers=teachers, students="")
            classroom.save()
            
            return Response(ClassroomSerializer(classroom).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JoinClassroomView(APIView):
    serializer_class = CreateClassroomSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            students = serializer.data.get("students")
            name = serializer.data.get("name")
            classroom = Classroom(name=name, teachers="", students=students)
            classroom.save()
            
            return Response(ClassroomSerializer(classroom).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateUserView(APIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            email = serializer.data.get("email")
            first_name = serializer.data.get("first_name")
            last_name = serializer.data.get("last_name")
            is_teacher = serializer.data.get("is_teacher")
            user = User(username=username, password=make_password(password), email=email, first_name=first_name, last_name=last_name, is_teacher=is_teacher)
            user.save()
            
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
