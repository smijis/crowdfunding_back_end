from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Fundraiser #telling Django "from the models.py file, import and read the Fundraiser class"
from .serializers import FundraiserSerializer #telling Django "from the serializer.py file, import and read the FundraiserSerializer class"

class FundraiserList(APIView): #creating our first view class and inheriting the rest framework's APIView. We will build our class on top of it so all classes I create should inherit it

    def get(self,request): #functions must match one of the http framework "get, post, patch, delete" - if you name it something else, it won't work
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = FundraiserSerializer(data=request.data)
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

