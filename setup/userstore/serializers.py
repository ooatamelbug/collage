from rest_framework import serializers
from .models import UserStore
from store.serializers import StoreSerializers

class UserStoreSerializers(serializers.ModelSerializer):
    class Meta:
        model= UserStore
        fields= '__all__'

