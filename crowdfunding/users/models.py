from django.contrib.auth.models import AbstractUser
from django.db import models 

class CustomUser(AbstractUser): #inheriting the built in default django AbstractUser class. Common practice to create your own "CustomUser" class
    is_active = models.BooleanField(default=True)
    def __str__(self): 
        return self.username #when you print to the console, you will get the username of the user
#make sure to edit the settings.py in crowdfunding to tell Django to use the CustomUser authentication
