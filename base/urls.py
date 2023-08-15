from django.urls import path
from .views import *

urlpatterns = [
    path('room_type/',roomTypeView,name='roomType'),
    path('room_type/<pk>',roomTypeDetailView,name='roomTypeDetail'),
    path('room/',RoomApiView.as_view(),name='room'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]