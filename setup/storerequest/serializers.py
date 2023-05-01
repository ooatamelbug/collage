from rest_framework import serializers
from .models import StoreRequest, RequestDrug

class StoreRequestSerializers(serializers.ModelSerializer):
    store_name = serializers.CharField(readOnly=True, source="store_store_request.store_name")
    class Meta:
        model= StoreRequest
        fields= '__all__'
        extra_fields = ['store_name']


class RequestDrugSerializers(serializers.ModelSerializer):
    drug_name = serializers.CharField(readOnly=True, source="drug_store_request.en_brand_name")
    class Meta:
        model= RequestDrug
        fields= '__all__'
        extra_ = ['drug_name']

