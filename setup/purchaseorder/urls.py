from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.PurchaseOrderApi.as_view()),
]