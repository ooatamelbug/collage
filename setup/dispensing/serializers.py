from rest_framework import serializers
from .models import Dispensing, SoldDrug

class DispensingSerializers(serializers.ModelSerializer):
    class Meta:
        model= Dispensing
        fields= '__all__'



class SoldDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model= SoldDrug
        fields= '__all__'