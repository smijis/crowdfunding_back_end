from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Fundraiser, Pledge #telling Django "from the models.py file, import and read the Fundraiser class"
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer #telling Django "from the serializer.py file, import and read the FundraiserSerializer class"

class FundraiserList(APIView): #creating our first view class and inheriting the rest framework's APIView. We will build our class on top of it so all classes I create should inherit it

    def get(self,request): #functions must match one of the http framework "get, post, patch, delete" - if you name it something else, it won't work
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid(): #if the data is valid in JSON format, serializer will save it
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FundraiserDetail(APIView): #inheriting the APIView
    def get(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk) #get this object or return 404 - store the data in the fundraiser variable
        serializer = FundraiserDetailSerializer(fundraiser) #running the fundraising variable and serializing the result - store the result in serializer variable
        return Response(serializer.data) #return serializer variable and exit the function

class PledgeList(APIView):

    def get(self,request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )