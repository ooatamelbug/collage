from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Drug, Classes
# from django.contrib.auth.models import User
from .serializers import ClassesSerializers, DrugSerializers
from responsibilities import serializers, models
from stock import models, serializers
# Create your views here.


class ClassesApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        classes = Classes.objects.all()
        serializerclasses = ClassesSerializers(classes, many= True)
        return Response(data=serializerclasses.data, status=200)

    def post(request):
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
        key = request.data.get('key')
        value = request.data.get('value')
        if key == 'en_brand_name':
            value = value.upper()
            data = Drug.objects.filter(en_brand_name__contains=value)
        elif key == 'chemical_name':
            data = Drug.objects.filter(chemical_name__contains=value)
        elif key == 'national_code':
            data = Drug.objects.filter(national_code__contains=value)
        elif key == 'class_id':
            data = Drug.objects.filter(class_id=value)
        else:
            data = Drug.objects.all()

        serializers = DrugSerializers(data, many=True)
        return Response(data=serializers.data, status=200)
