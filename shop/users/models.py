from django.db import models
from django.contrib.auth.models import User
import random,string,datetime
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField()

    def __str__(self):
        return self.name
    
class Otp(models.Model): 
    user=models.CharField(max_length=10,blank=True,null=True)
    otp=models.CharField(max_length=6)
    is_verified=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.is_verified
    

class Message(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    