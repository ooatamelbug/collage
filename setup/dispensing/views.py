from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import SoldDrug, Dispensing
from stock.models import Stock, StoreStock
from stock.serializers import StockSerializers
# from django.contrib.auth.models import User
from .serializers import DispensingSerializers, SoldDrugSerializers, CreateDispensingSerializers, CreateSoldDrugSerializers
from stock.serializers import StoreStockSerializers
from django.forms.models import model_to_dict
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
            serdrugInStock = StockSerializers(drugInStock, many=True)
            drugInStockAvailable = StoreStock.objects.filter(
                drug_id=drug['id'], store_id=request.data.get('store'))
            ser = StoreStockSerializers(drugInStockAvailable, many=True)
            if ser.data[0]['store_quantity'] < drug['quantity']:
                return Response("some items is not Available", status=404)
            total_price += serdrugInStock.data[0]['const_price'] * drug['quantity']

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
                serdrugInStock = StockSerializers(drugInStock, many=True)
                drugInStockAvailable = StoreStock.objects.filter(
                    drug_id=drug['id'], store_id=request.data.get('store'))
                ser = StoreStockSerializers(drugInStockAvailable, many=True)
                drugdetails = {
                    "sold_quantity": drug['quantity'],
                    "drug_id": drug['id'],
                    "store_stock_id": ser.data[0]['id'],
                    "dispensing_id": validate.data['id'],
                    "sell_price": serdrugInStock.data[0]['const_price'],
                }
                validatedrug = CreateSoldDrugSerializers(data=drugdetails)
                if validatedrug.is_valid(raise_exception=True):
                    validatedrug.save()
                    #  decrease  quantity
                    print(drugInStockAvailable)
                    data = {
                        "store_quantity": ser.data[0]['store_quantity'] - drug['quantity'],
                    }
                    serilizerStock = StoreStockSerializers(
                        drugInStockAvailable[0], data, partial=True)
                    if serilizerStock.is_valid(raise_exception=True):
                        serilizerStock.save()
                        print('d')
                    continue
            return Response(data=validate.data, status=201)


class Sales(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request):
        userid = request.query_params['user_id']
        storeid = request.query_params['store_id']
        to_date = request.query_params.get('to', None)
        from_date = request.query_params.get('from', None)
        date = request.query_params['date']
        total = 0
        amount = 0
        if (date is not None) and (from_date is None) and (to_date is None):
            total = Dispensing.objects.filter(
                user_id=userid, store_id=storeid, created_at__contains=date).count()

            dispens = Dispensing.objects.filter(
                user_id=userid, store_id=storeid, created_at__contains=date)
            serizler = DispensingSerializers(dispens, many=True)
            for data in serizler.data:
                amount += data['total_price']
        elif (from_date is not None) and (to_date is not None) and (date is None):
            total = Dispensing.objects.filter(
                user_id=userid, store_id=storeid, created_at__range=[from_date, to_date]).count()

            dispens = Dispensing.objects.filter(
                user_id=userid, store_id=storeid, create_at__range=[from_date, to_date])
            serizler = DispensingSerializers(dispens, many=True)
            for data in serizler.data:
                amount += data['total_price']

        return Response(data={"total_operation": total, "total_amount": amount}, status=200)
