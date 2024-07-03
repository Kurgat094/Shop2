from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('signin',signin,name="signin"),
    path('signup',signup,name="signup"),
    path('signout',signout,name="signout"),
    path('blogs',blogs,name='blogs'),
    path('services',services,name="services"),
    path('contact',contact,name="contact"),
    path('upload',upload_file,name="upload_file"),
    path('forgotpassword',forgotpassword,name="forgotpassword"),
    path('Otps',Otps,name='Otp'),
    path('resetpassword',resetpassword,name="resetpassword"),
    path('shop',shop,name="shop"),
    path('cart',cart,name='cart')
]
