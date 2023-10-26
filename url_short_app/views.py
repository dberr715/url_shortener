from .models import UserData, UrlData
from rest_framework import viewsets, status
from .serializers import (
    UserDataSerializer,
    UrlDataSerializer,
    CustomTokenObtainPairSerializer,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import redirect


# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all().order_by("-username")
    serializer_class = UserDataSerializer


class UrlDataViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = UrlData.objects.filter(userId=1).order_by("title")
    serializer_class = UrlDataSerializer


class RedirectView(APIView):
    model = UrlData

    def get(self, request, short_url):
        try:
            short_url = self.kwargs.get("short_url")
            urlObject = UrlData.objects.filter(short_url=short_url).values(
                "title", "original_url"
            )
            for item in urlObject:
                original_url = item["original_url"]
            response = redirect(original_url)
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
