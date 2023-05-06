from django.urls import path
from . import views

urlpatterns = [
    path('dispensing/', views.DispensingApi.as_view())
]