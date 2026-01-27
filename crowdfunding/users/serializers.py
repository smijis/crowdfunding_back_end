from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: #django pattern short for 'meta data' - tells it what model and fields to configure and include
        model = CustomUserfields = '__all__'
        extra_kwargs = {'password': {'write_only': True}} #kwargs = keyword arguments e.g. fn(food=bread, name=Sam)
        #serializers deserializes passwords into databases and when data goes out, it serializes. 'Write-only' means only send passwords, don't let any data out. Passwords can only be created, they can't be read by the API.

    def create(self, validated_data): #overwriting the default behaviour of the serializer
        return CustomUser.objects.create_user(**validated_data)
    #create_user is an inbuilt django feature. It tells serializer, when creating an account and data comes in, use the special function that looks out for the password field and will automatically hash it

