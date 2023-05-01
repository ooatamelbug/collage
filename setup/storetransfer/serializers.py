from rest_framework import serializers
from .models import StockTransfer, TransferDrug

class StockTransferSerializers(serializers.ModelSerializer):
    storerequest = serializers.CharField(readOnly=True, source="storerequest_stocktransfer")
    transferDrug = serializers.StringRelatedField(many=True)
    class Meta:
        model= StockTransfer
        fields= '__all__'
        extra_fields = ['storerequest', 'transferDrug']


class TransferDrugSerializers(serializers.ModelSerializer):
    drug_name = serializers.CharField(readOnly=True, source="drug_transfer_drug.en_brand_name")
    from_stock = serializers.CharField(readOnly=True, source="stocktransfer_stock_from.en_name")
    to_stock = serializers.CharField(readOnly=True, source="stocktransfer_stock_to.en_name")
    class Meta:
        model= TransferDrug
        fields= '__all__'
        extra_ = ['drug_name', 'from_stock', 'to_stock']

