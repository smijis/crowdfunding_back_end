from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser): #inheriting the built in default django AbstractUser class. Common practice to create your own "CustomUser" class
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    postcode = models.IntegerField(
    null=True, 
    blank=True,
    validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    def __str__(self): 
        return self.username #when you print to the console, you will get the username of the user
#make sure to edit the settings.py in crowdfunding to tell Django to use the CustomUser authentication
