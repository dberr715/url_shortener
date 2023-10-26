from .models import UserData
from .models import UrlData
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from django.contrib.auth import get_user_model

# User = get_user_model()


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["username", "password", "token"]


class UrlDataSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UrlData
        fields = ["title", "longUrl", "shortUrl", "userId"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, yo):
        data = super().validate(yo)

        data["userId"] = self.user.id
        data["username"] = self.user.username
        data["name"] = self.user.first_name + " " + self.user.last_name
        return data
