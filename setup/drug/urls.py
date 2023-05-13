from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.DrugApi.as_view()),
    path('classes/', views.ClassesApi.as_view())
]