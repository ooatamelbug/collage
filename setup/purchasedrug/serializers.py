from rest_framework import serializers
from .models import PurchaseDrug


class PurchaseDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDrug
        fields = '__all__'
        depth = 1

class CreatePurchaseDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDrug
        fields = ('order_quantity', 'invoice_quantity', 'drug_cost', 'drug_id', 'order_id')
