from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import SoldDrug, Dispensing
from stock.models import Stock, StoreStock
# from django.contrib.auth.models import User
from .serializers import DispensingSerializers, SoldDrugSerializers, CreateDispensingSerializers, CreateSoldDrugSerializers

# Create your views here.


class DispensingApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        print(id)
        if id is None:
            dispensing = Dispensing.objects.all()
            serilizer = DispensingSerializers(data=dispensing)
            return Response(serilizer.data, status=200)
        else:
            dispensing = Dispensing.objects.filter(id=request.data.id)
            if len(dispensing) == 0:
                return Response("no item with this data", status=404)
            else:
                serilizer = DispensingSerializers(data=dispensing)
                return Response(serilizer.data, status=200)

    def post(self, request):
        total_price = 0
        for drug in request.data.drugs:
            drugInStock = Stock.objects.filter(drug_id=drug.id)
            print(drugInStock)
            drugInStockAvailable = StoreStock.objects.filter(
                drug_id=drug.id, store_id=request.data.store)
            print(drugInStock)
            if drugInStockAvailable[0].store_quantity < drug.quantity:
                return Response("some items is not Available", status=404)
            total_price += drugInStock[0].const_price * drug.quantity
        print(total_price)
        dataSold = {
            "user_id": request.user.user_id,
            "total_price": total_price,
            "store_id": request.data.store,
        }
        validate = CreateDispensingSerializers(data=dataSold)
        if validate.is_valid():
            for drug in request.data.drugs:
                drugInStockAvailable = StoreStock.objects.filter(
                    drug_id=drug.id, store_id=request.data.store)
                drugdetails = {
                    "sold_quantity": drug.quantity,
                    "drug_id": drug.drug_id,
                    "store_stock_id": request.data.store,
                    "dispensing_id": validate.data.id,
                    "sell_price": drugInStockAvailable[0].const_price,
                }
                validatedrug = CreateSoldDrugSerializers(data=drugdetails)
                if validatedrug.is_valid():
                    continue
            return Response(data=validate.data, status=201)
