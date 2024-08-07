from django.shortcuts import render,redirect
from .forms import CreateUser,ProductForm,OtpForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from .models import Otp,Product
from django.core.mail import send_mail
import logging
import random
# Create your views here.



def home(request):
    return render(request,'home.html')


def signin(request):
    if request.method=="POST":
       form= AuthenticationForm(request,data=request.POST)
       if form.is_valid():
           username=form.cleaned_data.get('username')
           password=form.cleaned_data.get('password')
           user=authenticate(username=username,password=password)
           if user is not None:
                is_verified=Otp.objects.filter(is_verified=1)
                if is_verified:
                    login(request,user)
                    messages.success(request,f"You have loged in successfully")
                    return render(request,'shop.html')
                else:
                    messages.error(request,"please verify you accont")
                    return redirect('Otp')
    else :
        form=AuthenticationForm()
    return render(request,'login.html',{form :'form'})

logger = logging.getLogger(__name__)
def signup(request):
    form=CreateUser
    if request.method=='POST':
        form=CreateUser(request.POST)
        if form.is_valid():
            user=form.save()
            name=form.cleaned_data.get('username')
            group=Group.objects.get(name='users')
            user.groups.add(group)
            otp=random.randint(000000,999999)
            # is_user,created=Otp.objects.get_or_create(user=name)
            # is_user.user=name
            # is_user.otp=otp
            Otp.objects.create(user=user,otp=otp)
            # Send the email
            subject = "Successful Login Notification"
            message = f"""Hello,\n\nYou have successfully logged in to your account.
                         'Your Otp is ',
                         'Otp is :{otp},"""
            from_email = "tobiaskipkogei@gmail.com"  
            recipient_list = [user.email]
            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                logger.error(f"Error sending email: {e}")
            return redirect('Otp')
    context={
        "form":form
    }
    return render(request,'register.html',context)


def Otps(request):
    if request.method=="POST":
        user_otp=request.POST['otp']
        otp=Otp.objects.filter(otp=user_otp)
        if otp:
           is_verified=1
           verify,created=Otp.objects.get_or_create(otp=user_otp)
           verify.is_verified=int(is_verified)
           verify.save()
           return redirect('signin')
        else:
            return render(request,'otp.html')
    return render(request,'otp.html')

def forgotpassword(request):
    return render(request,'forgotpassword.html')

def resetpassword(request):
    if request.method=="POST":
        new_password=request.POST['newpassword']
        confirm=request.POST['confirm']
        if new_password==confirm:
            
            return redirect('signin')

    return render(request,'resetpassword.html')


def signout(request):
    logout(request)
    return redirect('signin')
def blogs(request):
    return render(request,'blogs.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')
    


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

def shop(request):
    products=Product.objects.all()
    return render(request,'shop.html',{'products':products})

def cart(request):
    return render(request,'cart.html')