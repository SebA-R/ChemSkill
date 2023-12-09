from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from rest_framework import generics, status
from .serializers import ClassroomSerializer, CreateClassroomSerializer, UserSerializer, JoinClassroomSerializer
from .models import Classroom, User
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import periodictable
import random


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
    serializer_class = JoinClassroomSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Retrieve the classroom from the database
            code = serializer.data.get("code")
            classroom = Classroom.objects.get(code=code)

            # Retrieve the student from the database
            student_username = request.data.get('username')
            student = User.objects.get(username=student_username)

            # Add the student to the classroom
            if classroom.students:
                classroom.students += ', ' + student.username
            else:
                classroom.students = student.username
            classroom.save()

            return Response(ClassroomSerializer(classroom).data, status=status.HTTP_200_OK)
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
    
class QuestionView(APIView):
    def metal():
        rand = random.randint(0, 11)
        metals = [2, 3, 10, 11, 18, 19, 36, 37, 54, 55, 86, 87]
        return metals[rand]


    def nonmetal():
        rand = random.randint(0, 8)
        nonmetals = [6, 7, 8, 14, 15, 16, 33, 34, 52]
        return nonmetals[rand]


    def charge(elm):
        metals = [2, 3, 10, 11, 18, 19, 36, 37, 54, 55, 86, 87]
        nonmetals = [6, 7, 8, 14, 15, 16, 33, 34, 52]
        for i in range(11):
            if (metals[i] == elm):
                return -(i % 2+1)
        if (elm == 6 or elm == 14):
            return 3
        elif (elm == 7 or elm == 15 or elm == 33):
            return 2
        else:
            return 1


    Elements = [
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P",
        "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru",
        "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce",
        "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
        "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
        "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
        "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Uut",
        "Fl", "Uup", "Lv", "Uus", "Uuo"]


    Molar_mass = {element.symbol: element.mass for element in periodictable.elements}


    def find_mass(Elements, Molar_mass):
        elm = random.randint(0, 117)
        mol = random.randint(1, 5)
        print("What is the mass of "+str(mol) +Elements[elm]+"?(round to the tenth decimal place)")

        ans = mol*Molar_mass[Elements[elm]]
        ans = round(ans, 1)
        # ans input here
        user_input = float(input())
        if (user_input == ans):
            print("correct")
        else:
            print("incorrect, the answer is: "+str(ans)+"g")

    def find_mol(Elements, Molar_mass):
        elm = random.randint(0, 117)
        m1 = Molar_mass[Elements[elm]]*random.randint(1, 5)+random.randint(1, 40)
        print("How many mols of "+Elements[elm]+" are present if there is "+str(
            m1)+"g?(round to the tenth decimal place)")

        ans = m1/Molar_mass[Elements[elm]]
        ans = round(ans, 1)
        # ans input here
        user_input = float(input())
        if (user_input == ans):
            print("correct")
        else:
            print("incorrect, the answer is: "+str(ans)+" mols.")

    def lim_reag(metal, nonmetal, charge, Elements, Molar_mass):
        elm1 = metal()
        elm2 = nonmetal()
        chg1 = charge(elm1)
        chg2 = charge(elm2)
        m1 = random.randint(1, 5)*Molar_mass[Elements[elm1]]+random.randint(1, 50)
        m2 = random.randint(1, 5)*Molar_mass[Elements[elm2]]+random.randint(1, 50)
        count1 = 1
        count2 = 1
        while (count1*chg1+count2*chg2 != 0):
            if (abs(count1*chg1) < abs(count2*chg2)):
                count1 += 1
            else:
                count2 += 1
        print("If "+str(m1)+" grams of "+Elements[elm1]+" reacted with "+str(m2)+" grams of "+Elements[elm2]+" creates " +
            Elements[elm1]+"("+str(count1)+")"+Elements[elm2]+"("+str(count2)+") which element is the limiting reageant?")
        user_input = input()
        if (m1/Molar_mass[Elements[elm1]] > m2/Molar_mass[Elements[elm2]]):
            ans = Elements[elm1]
        elif (m1/Molar_mass[Elements[elm1]] == m2/Molar_mass[Elements[elm2]]):
            ans = "N/A"
        else:
            ans = Elements[elm2]

        if (user_input == ans):
            print("correct")
        else:
            print("incorrect, the answer is: "+ans)
    
    def post(request):
        if request.data.get('question') == 'find-mass':
            return HttpResponse('find-mass')
    