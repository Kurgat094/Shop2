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
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now_add=True)
    def generate_otp(self):
        self.otp=''.join(random.choice(string.digits,k=6))
        self.created_at=datetime.datetime.now()
        self.save()
    
    def is_valid(self):
        now=datetime.datetime.now()
        return(now-self.created_at).total_seconds()<300

class Message(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    