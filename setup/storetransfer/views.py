from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import TransferDrug, StockTransfer
from storerequest.models import RequestDrug, StoreRequest
from storerequest.serializers import RequestDrugSerializers, StoreRequestSerializers
from .serializers import StockTransfer, StockTransferSerializers, TransferDrugSerializers, CreateStockTransferSerializers, CreateTransferDrugSerializers
from stock import models, serializers
# Create your views here.


class StockTransferDataAPI(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request):
        requestDrug = StockTransfer.objects.all()
        ser = StockTransferSerializers(requestDrug, many=True)
        return Response(data=ser.data, status=200)


class StockTransferAPI(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def post(self, request, pk=None, *args, **kwargs):
        requestDrug = RequestDrug.objects.get(pk=pk)
        if requestDrug == None:
            return Response(status=404)
        else:
            ser = RequestDrugSerializers(requestDrug)
            # request
            requestOrder = StoreRequest.objects.get(
                pk=ser.data['request_id']['id'])
            storeRequestSerializers = StoreRequestSerializers(requestOrder)

            stockTransfer = StockTransfer.objects.filter(
                request_id=ser.data['request_id']['id'])
            transfer = None
            if len(stockTransfer) <= 0:
                data = {
                    "request_id": ser.data['request_id']['id'],
                    "transfer_status": False,
                    "transfer_desc": "transefer " + str(ser.data['request_id']['id'])
                }
                requestDrugSerializers = CreateStockTransferSerializers(
                    data=data)
                requestDrugSerializers.is_valid(raise_exception=True)
                requestDrugSerializers.save()
                transfer = requestDrugSerializers.data
            else:
                requestDrugSerializers = CreateStockTransferSerializers(
                    stockTransfer, many=True)
                transfer = requestDrugSerializers.data[0]
            # here transfare drug from to
            errorArray = []
            for transferDrug in request.data.get('transferArray'):
                publisher = models.StoreStock.objects.filter(
                    store_id=transferDrug['from_stock'], drug_id=transferDrug['drug_id'])
                reciver = models.StoreStock.objects.filter(
                    store_id=transferDrug['to_stock'], drug_id=transferDrug['drug_id'])

                serpublisher = serializers.StoreStockSerializers(
                    publisher, many=True)
                serreciver = serializers.StoreStockSerializers(
                    reciver, many=True)
                # print(serreciver.data[0])
                drugtransfered = TransferDrug.objects.filter(
                    transfer_id=transfer['id'], drug_id=transferDrug['drug_id'], transfer_drug_status='REQ', to_stock_id=transferDrug['to_stock'])
                if len(drugtransfered) > 0:
                    errorArray.append(transferDrug)
                else:
                    datatranfer = {
                        "transfer_id": transfer['id'],
                        "drug_id": transferDrug['drug_id'],
                        "from_stock_id": serpublisher.data[0]['id'],
                        "to_stock_id": serreciver.data[0]['id'],
                        "transfer_drug_quantity": transferDrug['quantity'],
                        "transfer_drug_status": 'REQ',
                    }
                    # print(datatranfer)
                    create = CreateTransferDrugSerializers(data=datatranfer)
                    if create.is_valid() == False:
                        errorArray.append(transferDrug)

                    create.save()
                    # check if this store have enough
                    enoughDrug = models.StoreStock.objects.filter(
                        store_id=transferDrug['from_stock'], drug_id=transferDrug['drug_id'], store_quantity__gte=transferDrug['quantity'])
                    if len(enoughDrug) < 0:
                        errorArray.append(transferDrug)
                    else:
                        updatefrom = serializers.StoreStockSerializers(
                            instance=enoughDrug[0], data={"store_quantity": serpublisher.data[0]['store_quantity'] - transferDrug['quantity']})
                        findAnthor = models.StoreStock.objects.filter(
                            store_id=transferDrug['to_stock'], drug_id=transferDrug['drug_id'])
                        if len(findAnthor) > 0:
                            updateTo = serializers.StoreStockSerializers(
                                instance=findAnthor[0], data={"store_quantity": serreciver.data[0]['store_quantity'] + transferDrug['quantity']})
                            updatefrom.is_valid(raise_exception=True)
                            updateTo.is_valid(raise_exception=True)
                            updatefrom.save()
                            updateTo.save()
                            # update TransferDrugSerializers
                            updatetransfer = TransferDrug.objects.get(
                                pk=create.data['id'])
                            updatetransfer = TransferDrugSerializers(instance=updatetransfer, data={
                                "transfer_drug_status": 'CLS', "transfer_drug_quantity": create.data['transfer_drug_quantity']})
                            updatetransfer.is_valid(raise_exception=True)
                            updatetransfer.save()

                        # update request
                        serrequestDrug = RequestDrugSerializers(
                            instance=requestDrug, data={"request_status": "CLS", "request_drug_quantity": ser.data['request_drug_quantity']})
                        serrequestDrug.is_valid(raise_exception=True)
                        serrequestDrug.save()

                        continue
                    # update store
                    # update TransferDrugSerializers

            return Response(data={"error": errorArray}, status=200)
