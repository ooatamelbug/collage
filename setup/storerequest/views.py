from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import RequestDrug, StoreRequest
from .serializers import RequestDrugSerializers, StoreRequestSerializers, CreateRequestDrugSerializers, CreateStoreRequestSerializers

# Create your views here.


class DrugOrderRequest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        status = request.query_params.get('status')
        drugs = RequestDrug.objects.filter(request_status=status)
        serializer = RequestDrugSerializers(drugs, many=True)
        return Response(data=serializer.data, status=200)


class OrderAPI(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'put']

    def get(self, request):
        print(self, 'self')
        status = request.query_params.get('status')
        id = request.query_params.get('id')
        print(status, 'asdas')
        print(id, 'id')
        order = []
        if status is not None:
            order = StoreRequest.objects.filter(request_status=status)

        elif id is not None:
            order = StoreRequest.objects.filter(id=id)

        else:
            order = StoreRequest.objects.all()
            print(order, 'order')

        serlizer = StoreRequestSerializers(order, many=True)
        return Response(data=serlizer.data, status=200)

    def post(self, request):
        datarequest = {
            "store_id": request.data.get('store_id'),
            "user_id": request.user.id,
            "request_status": False,
            "request_desc": request.data.get('request_desc'),
        }
        validate = CreateStoreRequestSerializers(data=datarequest)
        if validate.is_valid(raise_exception=True):
            validate.save()
            for index, drug in enumerate(request.data.get('drugs')):
                drugdetails = {
                    "request_drug_quantity": drug['quantity'],
                    "drug_id": drug['id'],
                    "request_status": 'REQ',
                    "request_id": validate.data['id'],
                }
                validatedrug = CreateRequestDrugSerializers(data=drugdetails)
                if validatedrug.is_valid(raise_exception=True):
                    validatedrug.save()
                    #  decrease  quantity
                    continue
            return Response(data=validate.data, status=201)

    def put(self, request, pk=None):
            drugorder = RequestDrug.objects.get(pk=pk)
            if drugorder == None:
                return Response(data={"erro": "not"}, status=404)
            else:
                ser = CreateRequestDrugSerializers(
                    instance=drugorder, data=request.data, partial=True)
                ser.is_valid(raise_exception=True)
                ser.save()
                return Response(data="updated", status=200)   