from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
user_type_list = [('Frontdesk','Frontdesk'),('Restaurant','Restaurant'),('Accounting','Accounting'),('Management','Management')]

room_status_list = [('Available','Available'),('Unavailable','Unavailable')]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default='User',null=True)
    user_type = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class RoomType(models.Model):
    name = models.CharField(max_length=200)

class Room(models.Model):
    name = models.CharField(max_length=200)
    room_no = models.IntegerField()
    bed_count = models.IntegerField()
    status = models.CharField(max_length=20,choices=room_status_list)
    room_type = models.ForeignKey(RoomType,on_delete=models.CASCADE)

