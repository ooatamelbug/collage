from rest_framework import serializers
from .models import PurchaseOrder
from purchasedrug.serializers import PurchaseDrugSerializers


class PurchaseOrderSerializers(serializers.ModelSerializer):
    order_drug = PurchaseDrugSerializers(many=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        extra_fields = ['order_drug']
        depth= 1

class CreatePurchaseOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields ='__all__'
