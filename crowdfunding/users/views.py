from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserList(APIView): #this class lists all the users
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #tells serializer to tell model that the data is valid and save it
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CustomUserDetail(APIView): #inheriting on top of the built in API View. this class will deal with when we want to retrieve a particular user
    def get(self, request, pk): #pk = primary key e.g. /users/1 (1 is the primary key - the user ID)
        user = get_object_or_404(CustomUser, pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
class CustomAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True) #raise exception means raise an error
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email
        })