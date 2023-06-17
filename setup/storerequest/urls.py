from django.urls import path
from . import views

urlpatterns = [
    path('drugs/', views.DrugOrderRequest.as_view()),
    path('request/', views.OrderAPI.as_view()),
    path('request/<int:pk>/', views.OrderAPI.as_view()),
]