from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import ClassroomSerializer, CreateClassroomSerializer
from .models import Classroom
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
