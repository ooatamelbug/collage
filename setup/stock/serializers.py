from rest_framework import serializers
from .models import Stock, StoreStock

class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model= Stock
        fields= '__all__'


class StoreStockSerializers(serializers.ModelSerializer):
    drug: serializers.CharField(source="drug_stock_relation.en_brand_name")
    class Meta:
        model= StoreStock
        fields= '__all__'
        extra_fields= ['drug']