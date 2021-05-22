from django.test import TestCase
from django.contrib.auth import get_user_model

def sample_user(username="username@1", email=None,password="password"):
    """create a sample user"""
    return get_user_model().objects.create_user(username=username, email=email,password=password)

class ModelTests(TestCase):
    
    def test_create_user(self):
        """test create new user"""
        username = 'username@2'
        email = 'email@xyz.com'
        password = 'password2'

        user = get_user_model().objects.create_user(username=username, password=password, email=email)

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
    
    def test_email_blank_error(self):
        with self.assertRaises(ValueError):
            sample_user()

