from rest_framework import generics , permissions
from .serializers import RegisterSerializer , MyTokenObtainPairSerializer

from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
  permission_classes = [permissions.AllowAny]


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer