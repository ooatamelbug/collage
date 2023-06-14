from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserStore
from .serializers import UserStoreSerializers
from users.models import User
from store.models import Store
# Create your views here.

class UserStoreAPI(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request):
        data = UserStore.objects.all()
        serilzer = UserStoreSerializers(data, many= True)
        return Response(data=serilzer.data, status=200)
    
    def post(self, request):
        # data = User.objects.filter(id=request.data.get('user_id'))
        # store = Store.objects.filter(id=request.data.get('store_id'))
        # if len(data) > 0 and  len(store) > 0:
        serStore = UserStoreSerializers(data=request.data)
        serStore.is_valid()
        serStore.save()
        print(serStore.data)
            
        return Response(data=serStore.data, status=200)
        # else: 
        #     return Response(data={"message": "no"}, status=404)
