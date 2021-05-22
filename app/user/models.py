from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username,
            email=self.normalize_email(email),
        )
    
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):

    email = models.CharField(max_length=255, unique=True)
    objects = UserManager()
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'



