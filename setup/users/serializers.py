from rest_framework import serializers
from .models import User
from userstore.serializers import UserStoreSerializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class GetUserSerializers(serializers.ModelSerializer):
    store_userstore = UserStoreSerializers(many=True)
    class Meta:
        model = User
        exclude = '__all__'
