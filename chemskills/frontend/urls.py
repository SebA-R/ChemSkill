from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('classroom', index),
    path('classroom-join', index),
    path('classroom-create', index),
    path('login', index),
    path('register', index),
]
