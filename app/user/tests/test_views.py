from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

class TestCreateUser(TestCase):
    def setup(self):
        self.client = APIClient()
    
    def test_create_new_user(self):
        """Test user creation with valid payload success"""
        payload = {
            "email": "testuser@xyz.com",
            "password": "password",
            "username": 'testuser'
        }

        resp = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(resp.status_code,  status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**resp.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', resp.data)

