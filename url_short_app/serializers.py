from .models import UserData
from .models import UrlData
from rest_framework import serializers


class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ["username", "password", "token"]


class UrlDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UrlData
        fields = ["title", "longUrl", "shortUrl", "userId"]
