from rest_framework import serializers
from .models import PurchaseDrug


class PurchaseDrugSerializers(serializers.ModelSerializer):
    drug = serializers.CharField(readOnly=True, source="drugsdetails_drug.en_brand_name")
    class Meta:
        model = PurchaseDrug
        fields = '__all__'


class CreatePurchaseDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = PurchaseDrug
        fields = ('order_quantity', 'invoice_quantity', 'drug_cost', 'drug_id', 'order_id')
