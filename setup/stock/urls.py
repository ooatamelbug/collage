from django.urls import path
from . import views

urlpatterns = [
    path('shorts/', views.StockApi.as_view()),
    path('availability/', views.StoreStockApi.as_view())
]