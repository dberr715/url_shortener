
from .models import UserData, UrlData
from rest_framework import viewsets
from .serializers import UserDataSerializer, UrlDataSerializer


# Create your views here.
class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all().order_by("-username")
    serializer_class = UserDataSerializer

class UrlDataViewSet(viewsets.ModelViewSet):
    queryset = UrlData.objects.all().order_by("-title")
    serializer_class = UrlDataSerializer
