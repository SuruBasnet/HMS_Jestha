from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .permissions import FrontDeskUserPermission
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user != None:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    else:
        return Response(user)
    

# Create your views here.
@api_view(['GET','POST'])
def roomTypeView(request):
    if request.method == 'GET':
        room_type_objects = RoomType.objects.all()
        serializer = RoomTypeSerializer(room_type_objects,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def roomTypeDetailView(request,pk):
    if request.method == 'GET':
        try:
            room_type_obj = RoomType.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = RoomTypeSerializer(room_type_obj)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        try:
            room_type_obj = RoomType.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = RoomTypeSerializer(room_type_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        try:
            room_type_obj = RoomType.objects.get(id=pk)
        except:
            return Response('Data not found!')
        room_type_obj.delete()
        return Response('Data deleted!')


@api_view(['GET','POST'])
def roomView(request,pk):
    if request.method == 'GET':
        room_objects = Room.objects.filter(room_type=pk)
        serializer = RoomSerializer(room_objects,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        request.data['username'] = 'user'
        password = request.data.get("password")
        hash_password = make_password(password)
        request.data['password'] = hash_password
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('User created!')
        else:
            return Response(serializer.errors)

        
class RoomApiView(GenericAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['room_type','status']
    serializer_class = RoomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, FrontDeskUserPermission]

    def get(self,request):
        room_objects = Room.objects.all()
        filter_objects = self.filter_queryset(room_objects)
        serializer = self.serializer_class(filter_objects,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)