import pdb
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer for create user model"""
    class Meta:
        model=get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {"password": {'write_only': True, 'min_length': 5},
         }
    
    def create(self, validated_data):
        """create new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class AuthTokenSerializer(serializers.Serializer):
    """Serializer to validate credentials for token generation on login"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
       email = attrs['email']
       password = attrs['password']
       
       
       user = authenticate(
           request = self.context.get('request'),
           username=email,
           password=password
       )

       if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code='authorization')

       attrs['user'] = user
       return attrs
        
        
