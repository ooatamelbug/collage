from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    store_userstore = serializers.StringRelatedField(many=True)
    class Meta: 
        model = User
        exclude = ['password', 'store_userstore']
