from django.db import models

class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)

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