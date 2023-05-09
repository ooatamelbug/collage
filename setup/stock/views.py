from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from stock.models import Stock, StoreStock
# from django.contrib.auth.models import User
from .serializers import StockSerializers, StoreStockSerializers

# Create your views here.


class StockApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        storeStock = StoreStock.objects.filter(store_quantity__lte= 2)
        serilizer = StoreStockSerializers(data=storeStock)
        if len(storeStock) == 0:
            return Response("no item with this data", status=404)
        else:
            return Response(serilizer.data, status=200)
