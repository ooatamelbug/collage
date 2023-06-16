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
        serializerclasses = ClassesSerializers(classes, many=True)
        return Response(data=serializerclasses.data, status=200)

    def post(self, request):
        serializer = ClassesSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ClassesUCDApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        data= Classes.objects.get(pk=pk)
        serializer = ClassesSerializers(data)
        return  Response(data=serializer.data)
    

    def post(self, request):
        className = request.data.get('className')
        classFound = Classes.objects.filter(class_name=className)
        if len(classFound) > 0:
            return Response(data={"message": "exist"}, status=400)
        else:
            data = {"class_name":  className}
            serlizer = ClassesSerializers(data=data)
            serlizer.is_valid(raise_exception=True)
            serlizer.save()
            return Response(data=serlizer.data, status=201)

    def put(self, request, pk, format=None):
        className = request.data.get('className')
        classFound = Classes.objects.filter(id=pk)
        if len(classFound) < 0:
            return Response(data={"message": "NOT exist"}, status=404)
        else:
            data = {"class_name":  className}
            serlizer = ClassesSerializers(instance=classFound[0], data=data)
            serlizer.is_valid(raise_exception=True)
            serlizer.save()
            return Response(data=serlizer.data, status=201)

    def delete(self, request, pk, format=None):
        classFound = Classes.objects.get(id=pk)
        if len(classFound) < 0:
            return Response(data={"message": "NOT exist"}, status=404)
        else:
            classFound.delete()
            return Response(data="", status=200)


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
        national_code = request.data.get('national_code')
        chemical_name = request.data.get('chemical_name')
        class_id = request.data.get('class_id')
        if en_brand_name is not None:
            en_brand_name = en_brand_name.upper()
            data = Drug.objects.filter(en_brand_name__contains=en_brand_name)
        elif chemical_name is not None:
            data = Drug.objects.filter(chemical_name__contains=chemical_name)
        elif national_code is not None:
            data = Drug.objects.filter(national_code__contains=national_code)
        elif class_id is not None:
            data = Drug.objects.filter(class_id=class_id)
        else:
            data = Drug.objects.all()

        serializers = DrugSerializers(data, many=True)
        return Response(data=serializers.data, status=200)


class DrugUACApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        data= Drug.objects.get(pk=pk)
        serializer = DrugSerializers(data)
        return  Response(data=serializer.data)
    
    def post(self, request):
        serializer = DrugSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data={"message": "data saved"}, status=200)

    def put(self, request, pk, format=None):
        drugFound = Drug.objects.filter(id=pk)
        if len(drugFound) < 0:
            return Response(data={"message": "NOT exist"}, status=404)
        else:
            serlizer = DrugSerializers(
                instance=drugFound[0], data=request.data,  partial=True)
            serlizer.is_valid(raise_exception=True)
            serlizer.save()
            return Response(data=serlizer.data, status=201)
