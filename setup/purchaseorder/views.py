from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import PurchaseOrder
from purchasedrug.models import PurchaseOrder, PurchaseDrug
from stock.models import Stock, StoreStock
from .serializers import CreatePurchaseOrderSerializers, PurchaseOrderSerializers
from purchasedrug.serializers import CreatePurchaseDrugSerializers, PurchaseDrugSerializers
from stock.serializers import StockSerializers
from storerequest import models, serializers
from drug.models import Drug
from drug.serializers import DrugSerializers
# Create your views here.


class PurchaseOrderApi(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get', 'put']

    def get(self, request, pk=None, *args, **kwargs):
        print('here3')
        # id = kwargs.get('id')
        if pk is None:
            order = PurchaseOrder.objects.all()
            serilizer = PurchaseOrderSerializers(order, many=True)
            return Response(serilizer.data, status=200)
        else:
            order = PurchaseOrder.objects.filter(order_id=pk)
            if len(order) == 0:
                return Response("no item with this data", status=404)
            else:
                serilizer = PurchaseOrderSerializers(data=order[0])
                return Response(serilizer.data, status=200)

    def post(self, request):
        print('here')
        dataPurchase = {
            "order_status": 0,
            "order_desc": request.data.get('order_desc'),
            "store_id": request.data.get('store'),
            "invoice_status": request.data.get('invoice_status'),
            "supplier_id": request.data.get('supplier_id')
        }
        validate = CreatePurchaseOrderSerializers(data=dataPurchase)
        validate.is_valid(raise_exception=True)
        validate.save()
        for drug in request.data.get('details'):
            print(validate.data)
            drugdetails = {
                "order_quantity": drug['order_quantity'],
                "drug_id": drug['drug_id'],
                "order_id": validate.data['order_id'],
            }
            print('drugdetails')
            validatedrug = CreatePurchaseDrugSerializers(
                data=drugdetails, partial=True)
            validatedrug.is_valid(raise_exception=True)
            validatedrug.save()
            requestDrug = models.RequestDrug.objects.get(
                pk=drug['request_drug_num'])
            serilzerRequest = serializers.CreateRequestDrugSerializers(
                instance=requestDrug, data={"request_status": "CLS"}, partial=True)
            serilzerRequest.is_valid(raise_exception=True)
            serilzerRequest.save()
            continue

        return Response(data=validate.data, status=201)

    def put(self, request, id=None):
        print('here5')
        dataPurchase = PurchaseOrder.objects.get(pk=id)
        updatedata = {
            "invoice_number": request.data.get('invoice_number'),
            "invoice_atm": request.data.get('invoice_atm'),
        }

        serlizerPurchaseOrder = PurchaseOrderSerializers(
            instance=dataPurchase, data=updatedata, partial=True)
        serlizerPurchaseOrder.is_valid(raise_exception=True)
        serlizerPurchaseOrder.save()
        #
        for drug in request.data.get('details'):
            dataPurchasedetails = PurchaseDrug.objects.get(pk=drug['id'])
            detailsdata = {
                "invoice_quantity": drug['invoice_quantity'],
                "drug_cost": drug['drug_cost']
            }
            serlizerPurchaseDrug = CreatePurchaseDrugSerializers(
                instance=dataPurchasedetails, data=detailsdata, partial=True)
            serlizerPurchaseDrug.is_valid(raise_exception=True)
            serlizerPurchaseDrug.save()
            drugInStore = Stock.objects.filter(
                durg_id=serlizerPurchaseDrug.data['drug_id'])
            print(drugInStore)
            datastock = None
            if len(drugInStore) > 0:
                datastock = {
                    "stock_quantity": detailsdata['invoice_quantity'],
                    "const_price": detailsdata['drug_cost'],
                    "selling_price": detailsdata['drug_cost'],
                }

            else:
                drugdata = Drug.objects.get(pk=serlizerPurchaseDrug.data['drug_id'])
                seril = DrugSerializers(drugdata)
                datastock = {
                    "durg_id": seril.data['id'],
                    "ar_name": seril.data['ar_brand_name'],
                    "en_name": seril.data['en_brand_name'],
                    "stock_quantity": detailsdata['invoice_quantity'],
                    "const_price": detailsdata['drug_cost'],
                    "selling_price": detailsdata['drug_cost'],
                }
            serilzeStock = StockSerializers(
                instance=drugInStore[0], data=datastock, partial=True)
            serilzeStock.is_valid(raise_exception=True)
            serilzeStock.save()
            continue

        serlizerPurchaseOrder = CreatePurchaseOrderSerializers(
            instance=dataPurchase, data={"order_status": 1}, partial=True)
        serlizerPurchaseOrder.is_valid(raise_exception=True)
        serlizerPurchaseOrder.save()
        return Response(data="updated", status=200)
