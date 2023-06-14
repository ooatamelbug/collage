from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Store
from .serializers import StoreSerializers
# Create your views here.


class StoreAPI(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']

    def get(self, request):
        data = Store.objects.all()
        serStore = StoreSerializers(data, many=True)
        return Response(data=serStore.data, status=200)

    def post(self, request):
        serStore = StoreSerializers(data=request.data)
        serStore.is_valid(raise_exception=True)
        serStore.save()
        return Response(data=serStore.data, status=200)

    def put(self, request, pk):
        data = Store.objects.get(pk=pk)
        if len(data) <= 0:
            return Response(status=404)
        else:
            serStore = StoreSerializers(instance=data, data=request.data)
            serStore.is_valid(raise_exception=True)
            serStore.save()
        return Response(data=serStore.data, status=200)
