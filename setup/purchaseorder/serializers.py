from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializers(serializers.ModelSerializer):
    details = serializers.StringRelatedField(many=True)
    supplier = serializers.CharField(readOnly=True, source= "supplier_order.supplier_first_name")
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        extra_fields = ['details', 'supplier']


class CreatePurchaseOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ('order_desc', 'order_status', 'invoice_number', 'invoice_status', 'invoice_atm', 'supplier_id')
