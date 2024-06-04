from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Product,Otp

class CreateUser(UserCreationForm):
    email=forms.EmailField()
    class Meta:
      model=User
      fields=['username','email', 'password1','password2']


class ProductForm(forms.ModelForm):
   class Meta:
      model=Product
      fields=['name','description','price','image']

class OtpForm(forms.ModelForm):
   class Meta:
      modele=Otp
      fields=['otp']