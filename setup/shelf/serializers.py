from rest_framework import serializers
from .models import Shelf, ShelfDrug

class ShelfSerializers(serializers.ModelSerializer):
    class Meta:
        model= Shelf
        fields= '__all__'


class ShelfDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model= ShelfDrug
        fields= '__all__'