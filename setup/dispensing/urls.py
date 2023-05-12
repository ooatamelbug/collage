from django.urls import path
from . import views

urlpatterns = [
    path('operation/', views.DispensingApi.as_view()),
    path('sales/', views.Sales.as_view())
]