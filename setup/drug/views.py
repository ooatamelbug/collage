from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Drug 
# from django.contrib.auth.models import User
from .serializers import ClassesSerializers, DrugSerializers
from responsibilities import serializers, models

# Create your views here.


class ClassesApi(APIView):
    permission_classes = [IsAuthenticated]
    def createClasses(request):
        class_name = request.data.class_name
        serializer = ClassesSerializers(data={ class_name })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


class DrugApi(APIView):
    permission_classes = [IsAuthenticated]
    def post(request):
        en_brand_name = request.data.en_brand_name
        ar_brand_name = request.data.en_brand_name
        national_code = request.data.national_code
        class_id = request.data.class_id
        data = Drug.objects.all()
        if en_brand_name:
            data = Drug.objects.filter(en_brand_name=en_brand_name)
        if ar_brand_name:
            data = Drug.objects.filter(en_brand_name=ar_brand_name)
        if national_code:
            data = Drug.objects.filter(national_code=national_code)
        if class_id:
            data = Drug.objects.filter(class_id=class_id)
        
        serializers = DrugSerializers(data=data, many=True)
        return Response(data=serializers.data, status=200)