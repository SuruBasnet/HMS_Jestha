from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

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
