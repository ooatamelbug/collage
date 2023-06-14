from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializers(serializers.ModelSerializer):
    details = serializers.StringRelatedField(many=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        extra_fields = ['details']
        depth= 1

class CreatePurchaseOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ('order_desc', 'order_status', 'invoice_number', 'invoice_status', 'invoice_atm', 'supplier_id')
