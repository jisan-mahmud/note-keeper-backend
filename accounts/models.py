from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default= uuid.uuid4, unique= True,  primary_key= True, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"  # Login field
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email