from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Supplier
from .serializers import SupplierSerializers

# Create your views here.

class SupplierAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Suppliers = Supplier.objects.all()
        serilzer =  SupplierSerializers(Suppliers, many=True)
        return Response(data=serilzer.data, status=200)