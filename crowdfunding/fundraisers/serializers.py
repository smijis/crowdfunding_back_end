from rest_framework import serializers
from django.apps import apps

#serializer accepts the JSON data and deserializers it for the data

class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id') #can't change the owner or else it is bad logic if you can create fundraisers for anyone else
    owner_username = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.SerializerMethodField()
    fundraiser_title = serializers.ReadOnlyField(source='fundraiser.title')
    
    def get_supporter(self, obj):
        if obj.anonymous:
            return None
        return obj.supporter.username
    
    class Meta:
        model = apps.get_model('fundraisers.Pledge') #fundraisers folder's Pledge
        fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.suburb = validated_data.get('suburb', instance.suburb)
        instance.postcode = validated_data.get('postcode', instance.postcode)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    supporter = serializers.SerializerMethodField()

    def get_supporter(self, obj):
        if obj.anonymous:
            return None
        return obj.supporter.username

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.save()
        return instance
    
