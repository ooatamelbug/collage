from rest_framework import serializers
from .models import StoreRequest, RequestDrug


class RequestDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model= RequestDrug
        fields= '__all__'
        depth= 1


class StoreRequestSerializers(serializers.ModelSerializer):
    store_requested = RequestDrugSerializers(many=True)

    class Meta:
        model= StoreRequest
        fields= '__all__'
        depth= 1



class CreateRequestDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model= RequestDrug
        fields= ('drug_id', 'request_drug_quantity', 'request_status', 'request_id', 'id')


class CreateStoreRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model= StoreRequest
        fields= ('request_desc', 'request_status', 'store_id', 'user_id', 'id')
