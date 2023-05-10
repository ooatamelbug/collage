from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import SoldDrug, Dispensing
from stock.models import Stock, StoreStock
# from django.contrib.auth.models import User
from .serializers import DispensingSerializers, SoldDrugSerializers, CreateDispensingSerializers, CreateSoldDrugSerializers
from stock.serializers import StoreStockSerializers
# Create your views here.


class DispensingApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request, pk=None, *args, **kwargs):
        id = pk or request.query_params.get('id')
        if id is None:
            print('here')
            dispensing = Dispensing.objects.all()
            serilizer = DispensingSerializers(dispensing, many=True)

            return Response(data=serilizer.data, status=200)
        else:
            dispensing = Dispensing.objects.filter(id=request.data.id)
            if len(dispensing) == 0:
                return Response(data="no item with this data", status=404)
            else:
                serilizer = DispensingSerializers(data=dispensing)
                return Response(data=serilizer.data, status=200)

    def post(self, request):
        total_price = 0
        for index, drug in enumerate(request.data.get('drugs')):
            drugInStock = Stock.objects.filter(durg_id=drug['id'])
            drugInStockAvailable = StoreStock.objects.filter(
                drug_id=drug['id'], store_id=request.data.get('store'))
            if drugInStockAvailable[0].store_quantity < drug['quantity']:
                return Response("some items is not Available", status=404)
            total_price += drugInStock[0].const_price * drug['quantity']

        dataSold = {
            "user_id": request.user.id,
            "total_price": total_price,
            "store_id": request.data.get('store'),
        }
        validate = CreateDispensingSerializers(data=dataSold)
        if validate.is_valid():
            validate.save()
            for index, drug in enumerate(request.data.get('drugs')):
                drugInStock = Stock.objects.filter(durg_id=drug['id'])
                drugInStockAvailable = StoreStock.objects.filter(
                    drug_id=drug['id'], store_id=request.data.get('store'))
                drugdetails = {
                    "sold_quantity": drug['quantity'],
                    "drug_id": drug['id'],
                    "store_stock_id": drugInStockAvailable[0].id,
                    "dispensing_id": validate.data['id'],
                    "sell_price": drugInStock[0].const_price,
                }
                validatedrug = CreateSoldDrugSerializers(data=drugdetails)
                if validatedrug.is_valid(raise_exception=True):
                    validatedrug.save()
                    #  decrease  quantity
                    print(drugInStockAvailable)
                    data = {
                        "store_quantity": drugInStockAvailable[0].store_quantity - drug['quantity'],
                    }
                    serilizerStock = StoreStockSerializers(
                        drugInStockAvailable[0], data, partial=True)
                    if serilizerStock.is_valid(raise_exception=True):
                        serilizerStock.save()
                        print('d')
                    continue
            return Response(data=validate.data, status=201)
