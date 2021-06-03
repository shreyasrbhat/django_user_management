from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from django.urls import reverse
from rest_framework import status
import pdb


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
#UPDATE_USER_URL = reverse('user:update', kwargs={'username': 'testuser'})
#RETRIEVE_USER_URL = reverse('user:get', kwargs={'username': 'testuser'})
MANAGE_USER_URL = reverse('user:manage')

def create_new_user():
        payload = {
            "email": "testuser@xyz.com",
            "password": "password",
            "username": 'testuser',
        }
        user = get_user_model().objects.create_user(**payload)
        return user

class TestCreateUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        payload = {
            "email": "testuser@xyz.com",
            "password": "password",
            "username": 'testuser'
        }



    
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

class TokenAuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_create_valid_token(self):
        payload ={ "password": "password",
                    "email": 'testuser@xyz.com',
                 }
        user = create_new_user()
        resp = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', resp.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
    
    def test_token_invalid_credetials(self):
        user = create_new_user()
        payload ={ "password": "password_xyz",
                    "email": 'testuser@xyz.com',
                 }
        resp = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

class TestManageUserView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_new_user()
        self.client.force_authenticate(user=self.user)
    
    def test_retrive_user(self):
        resp = self.client.get(MANAGE_USER_URL)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.username, resp.data['username'])
        self.assertNotIn('password', resp.data)
    
    def test_update_user(self):
        """test update existing user"""
        payload = {
            "email": "testusernew@xyz.com",
            "password": "passwordnew",
            "username": 'testusernew'
        }
        resp = self.client.patch(MANAGE_USER_URL, payload)
        user = get_user_model().objects.get(username='testusernew')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, payload['username'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertEqual(user.email, payload['email'])





        
    


    
    # def test_update_user(self):
    #     user = create_new_user()
    #     factory = APIRequestFactory()
    #     # client = APIClient()
    #     # client.force_authenticate(user=user)

    #     #pdb.set_trace()
    #     update_details = {
    #         "email": "testuser2@xyz.com",
    #         "password": "password1",
    #         "username": 'testuser2'}

    #     view = RetrieveUpdateDeleteUser.as_view()
    #     request = factory.patch('/api/userupdate/', data=json.dumps(update_details), content_type='application/json')
    #     #request.user = user
    #     force_authenticate(request, user=user)
    #     pdb.set_trace()
    #     #resp = client.patch(UPDATE_USER_URL, data=json.dumps(update_details), content_type='application/json')
    #     resp = view(request, username='testuser')
    #     #user = get_user_model().objects.get(**resp.data)
    #     self.assertEqual(resp.status_code,  status.HTTP_200_OK)
    
    # # def test_retrieve_user(self):
    # #     user = create_new_user()
    # #     self.client = APIClient()
    # #     self.client.force_authenticate(user=user)
    # #     resp = self.client.get(RETRIEVE_USER_URL)
    # #     self.assertEqual(resp.status_code, status.HTTP_200_OK)

        
        

