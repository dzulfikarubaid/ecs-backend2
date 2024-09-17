from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'username': {'read_only': True},  # Username tidak dapat diubah
            'email': {'required': False},
            'name': {'required': False},
            'modul': {'required': False},
            'payment_status': {'required': False}
        }