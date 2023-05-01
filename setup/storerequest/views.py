from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import RequestDrug, StoreRequest
from .serializers import RequestDrugSerializers

# Create your views here.

class DrugOrderRequest(APIView):
    permission_classes = [IsAuthenticated]
    def getDrug(request):
        drugs = RequestDrug.objects.filter(request_status='REQ')
        serializer = RequestDrugSerializers(data=drugs, many= True)
        Response(data=serializer.data,status= 200)