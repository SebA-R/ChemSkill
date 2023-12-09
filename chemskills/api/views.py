from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import PermissionDenied
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
    serializer_class = ClassroomSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            students = serializer.data.get("students")
            name = serializer.data.get("name")
            classroom = Classroom(name=name, teachers="", students="")
            classroom.save()

            # Retrieve the student from the database
            student_username = request.data.get('student_username')
            student = User.objects.get(username=student_username)

            # Add the student to the classroom
            classroom.students.add(student)
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
            classrooms = serializer.data.get("classrooms")
            created_at = serializer.data.get("created_at")
            current_chapter = serializer.data.get("current_chapter")
            user = User(username=username, password=make_password(password), email=email, first_name=first_name, last_name=last_name, is_teacher=is_teacher, classrooms=classrooms, created_at=created_at, current_chapter=current_chapter)
            user.save()
            
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        password = self.request.query_params.get('password', None)
        if username is not None:
            obj = get_object_or_404(queryset, username=username)
            if check_password(password, obj.password):
                return obj
            else:
                raise PermissionDenied("Incorrect Password")
        return Response("Username is None", status=status.HTTP_400_BAD_REQUEST)
    