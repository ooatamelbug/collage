from rest_framework import serializers
from .models import StockTransfer, TransferDrug

class StockTransferSerializers(serializers.ModelSerializer):
    transferDrug = serializers.StringRelatedField(many=True)
    class Meta:
        model= StockTransfer
        fields= '__all__'
        extra_fields = [ 'transferDrug']
        depth = 1

class TransferDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model= TransferDrug
        fields= '__all__'
        depth = 1

