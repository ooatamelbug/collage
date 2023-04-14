from rest_framework import serializers
from .models import StoreRequest, RequestDrug

class StoreRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model= StoreRequest
        fields= '__all__'


class RequestDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model= RequestDrug
        fields= '__all__'

