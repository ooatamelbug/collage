from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Drug
# from django.contrib.auth.models import User
from .serializers import ClassesSerializers, DrugSerializers
from responsibilities import serializers, models
from stock import models, serializers
# Create your views here.


class ClassesApi(APIView):
    permission_classes = [IsAuthenticated]

    def createClasses(request):
        class_name = request.data.class_name
        serializer = ClassesSerializers(data={class_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DrugApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = request.query_params['id']
        store_id = request.query_params['store_id']
        if id != None:
            drug = Drug.objects.get(pk=id)
            serializerDrug = DrugSerializers(drug)
            stockData = models.StoreStock.objects.filter(
                drug_id=id, store_id=store_id)
            serializerstockData = serializers.StoreStockSerializers(
                stockData, many=True)
            return Response(data={"drug": serializerDrug.data, "store_stock": serializerstockData.data, }, status=200)
        else:
            return Response(data={"message": "not found"}, status=401)

    def post(self, request):
        en_brand_name = request.data.get('en_brand_name')
        if en_brand_name is not None:
            en_brand_name.upper()
        chemical_name = request.data.get('chemical_name')
        national_code = request.data.get('national_code')
        class_id = request.data.get('class_id')
        if en_brand_name:
            data = Drug.objects.filter(en_brand_name__contains=en_brand_name)
        elif chemical_name:
            data = Drug.objects.filter(chemical_name__contains=chemical_name)
        elif national_code:
            data = Drug.objects.filter(national_code__contains=national_code)
        elif class_id:
            data = Drug.objects.filter(class_id=class_id)
        else:
            data = Drug.objects.all()

        serializers = DrugSerializers(data, many=True)
        return Response(data=serializers.data, status=200)
