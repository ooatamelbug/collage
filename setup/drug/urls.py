from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.DrugApi.as_view())
]