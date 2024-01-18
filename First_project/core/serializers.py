from rest_framework import serializers
from core.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name', 'is_staff', 'date_joined']
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)