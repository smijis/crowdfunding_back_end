from django.db import models
from django.contrib.auth import get_user_model #django will get this from our AUTH_USER_MODEL in settings.py

class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(), #any other class, use the name of the model but for users, use the model we gave in the user setting. if we later change the model in the settings, we won't need to retype it everywhere 
        on_delete=models.CASCADE,
        related_name='owned_fundraisers'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser', #links to class Fundraiser (will automatically use the PK of the Fundraiser class)
        on_delete=models.CASCADE, #when a PK is deleted from Fundraiser class, casacade to the FK in the pledges table and remove all pledges associated with that PK
        related_name='pledges' #allows us to access all the pledges for that fundraiser
    )
    # other examples
    # 'Business' and related_name='investments'
    # 'Car' and related_name='products'

    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )