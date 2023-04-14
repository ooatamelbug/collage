from rest_framework import serializers
from .models import Responsibilities, UserResponsibilities

class ResponsibilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model= Responsibilities
        fields= '__all__'



class UserResponsibilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model= UserResponsibilities
        fields= '__all__'
