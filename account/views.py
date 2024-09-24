from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import Userserializer,LoginUserserializer,Userprofileserializer,Userchangepasswordserializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .renderers import UserRender
from rest_framework.permissions import IsAuthenticated


#generate manually generate
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class Userregistration(APIView):
    #renderer_classes=[UserRender]
    
    def post(self,request,format=None):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            #print(serializer.errors)
            return Response({'token':token,'msg':'successfull register'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    #renderer_classes=[UserRender]
    def post(self,request,format=None):
        serializer=LoginUserserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({"token":token,'msg':'login successful'},status=status.HTTP_200_OK)   
            else:
                return Response({'msg':'field_error'})

class UserProfileView(APIView):
    #renderer_classes=[UserRender]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=Userprofileserializer(data=request.user)
        #if serializer.is_valid():
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class Userchangepassword(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=Userchangepasswordserializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
        
            return Response({'msg':'successful password change'},status = status.HTTP_201_CREATED)

    
 