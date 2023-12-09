from django.urls import path
from .views import index, ClassroomView, CreateClassroomView, JoinClassroomView, UserView, CreateUserView

urlpatterns = [
    path('', index),
    path('classroom', ClassroomView.as_view()),
    path('create-classroom', CreateClassroomView.as_view()),
    path('join-classroom', JoinClassroomView.as_view()),
    path('user', UserView.as_view()),
    path('create-user', CreateUserView.as_view()),
]
