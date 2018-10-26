from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Please enter a first name"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Please enter a last name"
        if len(postData['email']) < 1:
            errors["email"] = "Please enter an email"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address ex. 'yourname@email.com'"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()