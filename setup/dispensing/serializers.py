from rest_framework import serializers
from .models import Dispensing, SoldDrug



class CreateDispensingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dispensing
        fields = ('user_id', 'total_price', 'store_id', 'id')


class SoldDrugSerializers(serializers.ModelSerializer):
    drug: serializers.CharField(source="drug_stock_relation.en_brand_name")
    class Meta:
        model = SoldDrug
        fields = '__all__'
        depth= 1

class CreateSoldDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = SoldDrug
        fields = ('drug_id', 'store_stock_id', 'dispensing_id',
                  'sell_price', 'sold_quantity')


class DispensingSerializers(serializers.ModelSerializer):
    dispensing_drug = SoldDrugSerializers(many=True)

    class Meta:
        model = Dispensing
        fields = '__all__'