from django.urls import path
from . import views

urlpatterns = [
    path('dispensing/', views.DrugApi.as_view())
]