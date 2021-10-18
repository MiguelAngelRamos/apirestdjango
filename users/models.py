from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
    """email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'# para hacer login con email
    REQUIRED_FIELDS = [] # Es necesario cada vez que usamos el  USERNAME_FIELD"""