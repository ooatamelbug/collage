from rest_framework import serializers
from .models import Dispensing, SoldDrug


class DispensingSerializers(serializers.ModelSerializer):
    soldDrugs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Dispensing
        fields = '__all__'
        extra_fields = ['soldDrugs']


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
