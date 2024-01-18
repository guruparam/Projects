
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer

# Create a CustomUser Model.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
