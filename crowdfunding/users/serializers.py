from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from fundraisers.serializers import FundraiserSerializer, PledgeSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: #django pattern short for 'meta data' - tells it what model and fields to configure and include
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}} #kwargs = keyword arguments e.g. fn(food=bread, name=Sam)
        #serializers deserializes passwords into databases and when data goes out, it serializes. 'Write-only' means only send passwords, don't let any data out. Passwords can only be created, they can't be read by the API.

    def create(self, validated_data): #overwriting the default behaviour of the serializer
        return CustomUser.objects.create_user(**validated_data)
    #create_user is an inbuilt django feature. It tells serializer, when creating an account and data comes in, use the special function that looks out for the password field and will automatically hash it

class UserDetailSerializer(serializers.ModelSerializer):
    fundraisers = FundraiserSerializer(many=True, read_only=True, source='owned_fundraisers')
    pledges = PledgeSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'name', 'email', 'suburb', 'postcode', 'fundraisers', 'pledges']