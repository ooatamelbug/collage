from rest_framework import serializers
from .models import StockTransfer, TransferDrug


class CreateStockTransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = StockTransfer
        fields = '__all__'


class CreateTransferDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransferDrug
        fields = '__all__'

class TransferDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransferDrug
        fields = '__all__'
        depth = 1


class StockTransferSerializers(serializers.ModelSerializer):
    stock_transfer_transfer_drug = TransferDrugSerializers(many=True)

    class Meta:
        model = StockTransfer
        fields = '__all__'
        extra_fields = ['stock_transfer_transfer_drug']
        depth = 1


