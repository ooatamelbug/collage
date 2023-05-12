from rest_framework import serializers
from .models import Drug, Classes

class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model= Classes
        fields= '__all__'



class DrugSerializers(serializers.ModelSerializer):
    class Meta:
        model= Drug
        fields= '__all__'
      