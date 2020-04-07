from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100) # Name has maximum length of 100 characters
    email = models.EmailField(max_length=100, unique=True) # Email has max length of 100 & must be unique
    message = models.CharField(max_length=500, blank=True) # Max length of message is 500 chars, optional
    created_at = models.DateTimeField(auto_now_add=True) # Use current datetime value for attribute

# Migrate the models by running the following commands in shell:
# $python manage.py makemigrations |app_name|
# $python manage.py migrate