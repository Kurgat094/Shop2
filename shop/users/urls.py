from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('signin',signin,name="signin"),
    path('signup',signup,name="signup"),
    path('blogs',blogs,name='blogs'),
    path('services',services,name="services"),
    path('contact',contact,name="contact"),
    path('upload_file',upload_file,name="upload_file"),
    path('forgotpassword',forgotpassword,name="forgotpassword"),
    path('otp',otp,name='otp'),
    path('resetpassword',resetpassword,name="resetpassword"),
]
