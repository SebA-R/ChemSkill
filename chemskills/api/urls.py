from django.urls import path
from .views import index, ClassroomView, CreateClassroomView

urlpatterns = [
    path('', index),
    path('room', ClassroomView.as_view()),
    path('create-room', CreateClassroomView.as_view())
]
