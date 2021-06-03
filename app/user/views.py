from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.db.models import query
from rest_framework import generics, authentication

from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings



class CreateUserView(generics.CreateAPIView):
    """create a new user"""
    serializer_class = UserSerializer

class AuthTokenView(ObtainAuthToken):
    """Generate new auth token"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Retrive or update user profile"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_object(self):
        return self.request.user



        


    
