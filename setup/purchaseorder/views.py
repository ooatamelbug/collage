from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import PurchaseOrder
from purchasedrug.models import PurchaseOrder
from stock.models import Stock, StoreStock
# from django.contrib.auth.models import User
from .serializers import  CreatePurchaseOrderSerializers, PurchaseOrderSerializers
from purchasedrug.serializers import CreatePurchaseDrugSerializers, PurchaseDrugSerializers

# Create your views here.


class DispensingApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is None:
            order = PurchaseOrder.objects.all()
            serilizer = PurchaseOrderSerializers(data=order)
            return Response(serilizer.data, status=200)
        else:
            order = PurchaseOrder.objects.filter(id=request.data.id)
            if len(order) == 0:
                return Response("no item with this data", status=404)
            else:
                serilizer = PurchaseOrderSerializers(data=order)
                return Response(serilizer.data, status=200)

    def post(self, request):
        dataPurchase = {
            "invoice_number": request.data.invoice_number,
            "order_status": 0,
            "order_desc": request.data.order_desc,
            "store_id": request.data.store,
            "invoice_status": request.data.invoice_status,
            "invoice_atm": request.data.invoice_atm,
            "supplier_id": request.data.supplier_id
        }
        validate = CreatePurchaseOrderSerializers(data=dataPurchase)
        if validate.is_valid():
            for drug in request.data.details:
                drugdetails = {
                    "order_quantity": drug.order_quantity,
                    "drug_cost": drug.drug_cost,
                    "drug_id": drug.drug_id,
                    "invoice_quantity": request.data.invoice_quantity,
                    "order_id": validate.data.id,
                }
                validatedrug = CreatePurchaseDrugSerializers(data=drugdetails)
                if validatedrug.is_valid():
                    continue
            return Response(data=validate.data, status=201)
