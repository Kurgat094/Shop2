from django.shortcuts import render,redirect
from .forms import CreateUser,ProductForm,OtpForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import Otp
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'home.html')


def signin(request):
    if request.method=="POST":
       form= AuthenticationForm(request,data=request.POST)
       if form.is_valid:
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password')
           user=authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               messages.success(request,f"You have loged in successfully")
               return render(request,'shop.html')
    else :
        form=AuthenticationForm()
    return render(request,'login.html',{form :'form'})


def signup(request):
    form=CreateUser
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='users')
            user.groups.add(group)
            return redirect('signin')
    context={
        "form":form
    }
    return render(request,'register.html',context)
    

def blogs(request):
    return render(request,'blogs.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')
    
def otp(request):
    return render(request,'otp.html')

def forgotpassword(request):
    return render(request,'forgotpasssword.html')

def upload_file(request):
    form=ProductForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='product')
            user.groups.add(group)
            messages.success(request,f"You are successfully aploaded your products")
            return render(request,'admin.html')
    return render(request,'admin.html',{"form":form})

def send_otp_email(user,otp):
    send_mail(
        'Your Otp is ',
        f'Otp is :{otp}',
        
    )
