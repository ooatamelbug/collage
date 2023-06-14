from django.urls import path
from . import views

urlpatterns = [
    path('getUser/', views.getOneUser),
    path('createUser/', views.createUser),
    path('getall/', views.getall),
]