from django.urls import path
from . import views

urlpatterns = [
    path('data/<int:pk>/', views.StockTransferAPI.as_view()),
    path('get/data/', views.StockTransferDataAPI.as_view()),
]