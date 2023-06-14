from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import PurchaseOrder
from purchasedrug.models import PurchaseOrder
from stock.models import Stock, StoreStock
from .serializers import CreatePurchaseOrderSerializers, PurchaseOrderSerializers
from purchasedrug.serializers import CreatePurchaseDrugSerializers, PurchaseDrugSerializers
from stock.serializers import StockSerializers

# Create your views here.


class PurchaseOrderApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is None:
            order = PurchaseOrder.objects.all()
            serilizer = PurchaseOrderSerializers(order, many=True)
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
            "order_status": 0,
            "order_desc": request.data.order_desc,
            "store_id": request.data.store,
            "invoice_status": request.data.invoice_status,
            "supplier_id": request.data.supplier_id
        }
        validate = CreatePurchaseOrderSerializers(data=dataPurchase)
        if validate.is_valid():
            for drug in request.data.details:
                drugdetails = {
                    "order_quantity": drug.order_quantity,
                    "drug_id": drug.drug_id,
                    "order_id": validate.data.id,
                }
                validatedrug = CreatePurchaseDrugSerializers(data=drugdetails)
                if validatedrug.is_valid():
                    continue
            return Response(data=validate.data, status=201)

    def put(self, request, pk):
        dataPurchase = PurchaseOrder.objects.get(id=pk)
        updatedata = {
            "invoice_number": request.data.get('invoice_number'),
            "invoice_atm": request.data.get('invoice_atm'),
        }

        serlizerPurchaseOrder = PurchaseOrderSerializers(
            instance=dataPurchase, data=updatedata)
        serlizerPurchaseOrder.is_valid(raise_exception=True)
        serlizerPurchaseOrder.save()
        #
        for drug in request.data.details:
            dataPurchasedetails = PurchaseOrder.objects.get(id=drug.id)
            detailsdata = {
                "invoice_quantity": drug.invoice_quantity,
                "drug_cost": drug.drug_cost
            }
            serlizerPurchaseDrug = PurchaseDrugSerializers(
                instance=dataPurchasedetails, data=detailsdata)
            serlizerPurchaseDrug.is_valid(raise_exception=True)
            serlizerPurchaseDrug.save()
            drugInStore = Stock.objects.get(
                drug_id=serlizerPurchaseDrug.data['drug_id'])
            if len(drugInStore) > 0:
                data = {
                    "stock_quantity": detailsdata['invoice_quantity'],
                    "const_price": detailsdata['drug_cost'],
                    "selling_price": detailsdata['drug_cost'],
                }
                serilzeStock = StockSerializers(
                    instance=drugInStore[0], data=data)
                serilzeStock.is_valid(raise_exception=True)
                serilzeStock.save()
            continue
        serlizerPurchaseOrder = PurchaseOrderSerializers(
            instance=dataPurchase, data={"order_status": 1})
        serlizerPurchaseOrder.is_valid(raise_exception=True)
        serlizerPurchaseOrder.save()
        return Response(data="updated", status=200)
