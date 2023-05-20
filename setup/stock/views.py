from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Stock, StoreStock
# from django.contrib.auth.models import User
from .serializers import StockSerializers, StoreStockSerializers, StoreStockSerializersLite
from django.core.exceptions import ObjectDoesNotExist
import collections
# Create your views here.


class StockApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        storeStock = StoreStock.objects.filter(store_quantity__lte=2)
        serilizer = StoreStockSerializers(storeStock, many=True)
        if len(storeStock) == 0:
            return Response(data="no item with this data", status=404)
        else:
            return Response(data=serilizer.data, status=200)


class StoreStockApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        try:
            storeStock = StoreStock.objects.get(pk=id)
            serilizer = StoreStockSerializersLite(storeStock)
            data = serilizer.data
            d = collections.OrderedDict()
            
            inother = StoreStock.objects.filter(
                drug_id=data['drug_id'], store_quantity__gt=0).exclude(store_id=data['store_id'])
            serilizerd = StoreStockSerializers(inother, many=True)
            return Response(data=serilizerd.data, status=200)
        except ObjectDoesNotExist:
            return Response(data="no item with this data", status=404)
