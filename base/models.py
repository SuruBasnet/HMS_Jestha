from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
user_type_list = [('Frontdesk','Frontdesk'),('Restaurant','Restaurant'),('Accounting','Accounting'),('Management','Management')]

room_status_list = [('Available','Available'),('Unavailable','Unavailable')]

gender_list = [('Male','Male'),('Female','Female'),('Others','Others')]

bill_status_list = [('Paid','Paid'),('Unpaid','Unpaid')]

payment_method_list = [('Online','Online'),('Offline','Offline')]

food_type_list = [('Veg','Veg'),('Non-veg','Non-veg')]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default='User',null=True)
    user_type = models.CharField(max_length=20,choices=user_type_list)

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

class CustomerDetail(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=200,choices=gender_list)
    work = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(unique=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)

class Bill(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    amount = models.IntegerField()
    status = models.CharField(max_length=200)
    date = models.DateField()
    customer_detail = models.ForeignKey(CustomerDetail,on_delete=models.CASCADE)

class PaymentInfo(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    paid_amount = models.IntegerField()
    payment_method = models.CharField(max_length=100,choices=payment_method_list)

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=50,choices=gender_list)
    joining_date = models.DateField()
    salary = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class MenuType(models.Model):
    name = models.CharField(max_length=300)

class Food(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    food_type = models.CharField(max_length=200,choices=food_type_list)
    price = models.IntegerField()
    menu_type = models.ForeignKey(MenuType,on_delete=models.SET_NULL,null=True)
    
class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()

class Facilities(Service):
    pass