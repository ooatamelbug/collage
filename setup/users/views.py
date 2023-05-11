from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
# from django.contrib.auth.models import User
from .serializers import UserSerializers, GetUserSerializers
from responsibilities import serializers, models
from userstore.models import UserStore
from userstore.serializers import UserStoreSerializers
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOneUser(request):
    user = User.objects.get(username=request.user.username)
    userRes = models.UserResponsibilities.objects.filter(user_id=request.user.id)
    serializerUser = UserSerializers(user)
    stored = UserStore.objects.filter(user_id=request.user.id)
    store = UserStoreSerializers(stored, many=True)
    print(store)
    serializerUserResponsibilities = serializers.UserResponsibilitiesSerializers(userRes, many=True)
    data = { 'user': serializerUser.data, 'store': store.data, 'responsibilities': serializerUserResponsibilities.data }
    return Response(data=data, status=200)