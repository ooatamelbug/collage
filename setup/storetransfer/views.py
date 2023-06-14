from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import TransferDrug
from storerequest.models import RequestDrug, StoreRequest
from storerequest.serializers import RequestDrugSerializers, StoreRequestSerializers
from .serializers import StockTransfer, StockTransferSerializers, TransferDrugSerializers
from stock import models, serializers
# Create your views here.


class StockTransferAPI(APIView):
    def post(self, request, pk):
        requestDrug = RequestDrug.objects.get(pk=pk)
        if len(requestDrug) <= 0:
            return Response(status=404)
        else:
            ser = RequestDrugSerializers(requestDrug)
            # request
            requestOrder = StoreRequest.objects.get(pk=ser.data['request_id'])
            storeRequestSerializers = StoreRequestSerializers(requestOrder)

            stockTransfer = StockTransfer.objects.get(
                request_id=ser.data['request_id'])
            transfer = None
            if len(stockTransfer) <= 0:
                data = {
                    "request_id": ser.data['request_id'],
                    "transfer_status": False,
                    "transfer_desc": "transefer " + ser.data['request_id']
                }
                requestDrugSerializers = RequestDrugSerializers(data=data)
                requestDrugSerializers.is_valid(raise_exception=True)
                requestDrugSerializers.save()
                transfer = requestDrugSerializers.data
            else:
                requestDrugSerializers = RequestDrugSerializers(stockTransfer)
                transfer = requestDrugSerializers.data
            # here transfare drug from to
            errorArray = []
            for transferDrug in request.data.get('transferArray'):
                drugtransfered = TransferDrug.objects.get(
                    transfer_id=transfer['id'], drug_id=transferDrug['drug_id'], transfer_drug_status='REQ', to_stock_id=transferDrug['to_stock'])
                if len(drugtransfered) > 0:
                    errorArray.append(transferDrug)
                else:
                    data = {
                        "transfer_id": transfer['id'],
                        "drug_id": transferDrug['drug_id'],
                        "from_stock_id": transferDrug['from_stock'],
                        "to_stock_id": transferDrug['to_stock'],
                        "transfer_drug_quantity": transferDrug['quantity'],
                        "transfer_drug_status": 'REQ',
                    }
                    create = TransferDrugSerializers(data=data)
                    if create.is_valid() != False:
                        errorArray.append(transferDrug)
                    else:
                        create.save()
                    # check if this store have enough
                    enoughDrug = models.StoreStock.objects.get(
                        store_id=transferDrug['from_stock'], drug_id=transferDrug['drug_id'], store_quantity__gte=transferDrug['quantity'])
                    if len(enoughDrug) < 0:
                        errorArray.append(transferDrug)
                    else:
                        updatefrom = serializers.StoreStockSerializers(
                            instance=enoughDrug[0], data={"store_quantity": -transferDrug['quantity']})
                        findAnthor = models.StoreStock.objects.get(
                            store_id=transferDrug['to_stock'], drug_id=transferDrug['drug_id'])
                        if len(findAnthor) > 0:
                            updateTo = serializers.StoreStockSerializers(instance=findAnthor[0], data={"store_quantity": +transferDrug['quantity']})
                            updatefrom.is_valid(raise_exception=True)
                            updateTo.is_valid(raise_exception=True)
                            updatefrom.save()
                            updateTo.save()
                            #update TransferDrugSerializers
                            updatetransfer = TransferDrug.objects.get(pk=create.data['id'])
                            updatetransfer = TransferDrugSerializers(instance=updatetransfer, data={"transfer_drug_status": 'CLS'})
                            updatetransfer.is_valid()
                            updatetransfer.save()

                    # update store
                    # update TransferDrugSerializers

                return Response(data={"error": errorArray}, status=200)
