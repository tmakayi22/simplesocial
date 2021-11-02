from django.db import models
from django.contrib import auth


# Create User models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username) # built in in User
