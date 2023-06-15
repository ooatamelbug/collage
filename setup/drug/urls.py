from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.DrugApi.as_view()),
    path('classes/', views.ClassesApi.as_view()),
    path('classes/operation/', views.ClassesUCDApi.as_view()),
    path('drug/operation/', views.DrugUACApi.as_view()),
    path('drug/operation/<int:pk>/', views.DrugUACApi.as_view()),
    path('classes/operation/<int:pk>/', views.ClassesUCDApi.as_view()),
]