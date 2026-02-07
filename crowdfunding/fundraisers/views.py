from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Fundraiser, Pledge #telling Django "from the models.py file, import and read the Fundraiser class"
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer, PledgeDetailSerializer #telling Django "from the serializer.py file, import and read the FundraiserSerializer class"
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

class FundraiserList(APIView): #creating our first view class and inheriting the rest framework's APIView. We will build our class on top of it so all classes I create should inherit it
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #don't need to check that the user is the owner for get and post

    def get(self,request): #functions must match one of the http framework "get, post, patch, delete" - if you name it something else, it won't work
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid(): #if the data is valid in JSON format, serializer will save it
            serializer.save(owner=request.user) #use the current user who is logged in
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FundraiserDetail(APIView): #inheriting the APIView. (Shorter version by Biago)
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly #a custom class we made for our specific fundraiser
    ]

    def get(self, request, pk): #It is in the fundraiser detail view because this is related to the url that has the number (primary key) e.g. /fundraisers/1/
        fundraiser = get_object_or_404(Fundraiser, pk=pk) #get this object or return 404 - store the data in the fundraiser variable
        serializer = FundraiserDetailSerializer(fundraiser) #running the fundraising variable and serializing the result - store the result in serializer variable
        return Response(serializer.data) #return serializer variable and exit the function

    def put(self, request, pk): #updating an existing fundraiser. It is in the fundraiser detail view because this is related to the url that has the number (primary key) e.g. /fundraisers/1/
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        self.check_object_permissions(request, fundraiser) #!!!if user must be owner, YOU MUST HAVE THIS LINE (this is from 'permissions' file)
        serializer = FundraiserDetailSerializer(
            instance = fundraiser, #the specific fundraiser instance
            data = request.data, #data of the updated JSON fields
            partial = True
        )
        if serializer.is_valid():
            serializer.save() #it is safe to save the update
            return Response(serializer.data) #return the data that we saved
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user) #use the current user who is logged in
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]

    def get(self, request, pk):      #this one needs the id in the URL (the get above doesn't)   
        pledge = get_object_or_404(Pledge, pk=pk) 
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk)
        self.check_object_permissions(request, pledge)
        serializer = PledgeDetailSerializer(
            instance = pledge,
            data = request.data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data) 
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk)
        self.check_object_permissions(request, pledge)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)