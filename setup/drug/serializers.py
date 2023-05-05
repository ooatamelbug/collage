from rest_framework import serializers
from .models import Drug, Classes

class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model= Classes
        fields= '__all__'



class DrugSerializers(serializers.ModelSerializer):
    store = serializers.StringRelatedField(many=True)
    class Meta:
        model= Drug
        fields= '__all__'
        extra_fields = ['store']