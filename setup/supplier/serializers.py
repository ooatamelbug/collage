from rest_framework import serializers
from .models import Supplier

class SupplierSerializers(serializers.ModelSerializer):
    class Meta:
        model= Supplier
        fields= '__all__'

