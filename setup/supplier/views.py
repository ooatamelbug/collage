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
        suppliers = Supplier.objects.all()
        serilzer = SupplierSerializers(suppliers, many=True)
        return Response(data=serilzer.data, status=200)

    def post(self, request):
        serilzer = SupplierSerializers(data=request.data)
        serilzer.is_valid(raise_exception=True)
        serilzer.save()
        return Response(data=serilzer.data, status=201)

    def put(self, request, pk):
        suppliers = Supplier.objects.get(id=pk)
        serilzer = SupplierSerializers(instance=suppliers, data=request.data)
        serilzer.is_valid(raise_exception=True)
        serilzer.save()
        return Response(data=serilzer.data, status=201)
