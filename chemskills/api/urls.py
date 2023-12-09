from django.urls import path
from .views import index, ClassroomView, CreateClassroomView, JoinClassroomView, UserView, CreateUserView

urlpatterns = [
    path('', index),
    path('room', ClassroomView.as_view()),
    path('create-room', CreateClassroomView.as_view()),
    path('join-room', JoinClassroomView.as_view()),
    path('user', UserView.as_view()),
    path('create-user', CreateUserView.as_view())
]
