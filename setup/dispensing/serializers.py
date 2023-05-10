from rest_framework import serializers
from .models import Dispensing, SoldDrug



class CreateDispensingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dispensing
        fields = ('user_id', 'total_price', 'store_id')


class SoldDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = SoldDrug
        fields = '__all__'


class CreateSoldDrugSerializers(serializers.ModelSerializer):
    class Meta:
        model = SoldDrug
        fields = ('drug_id', 'store_stock_id', 'dispensing_id',
                  'sell_price', 'sold_quantity')


class DispensingSerializers(serializers.ModelSerializer):
    dispensing_drug_set = SoldDrugSerializers(many=True)

    class Meta:
        model = Dispensing
        fields = ('id', 'dispensing_drug_set', 'user_id', 'store_id', 'total_price')