from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    """Serializer for create user model"""
    class Meta:
        model=get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {"password": {'write_only': True, 'min_length': 5}}
    
    def create(self, validated_data):
        """create new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
