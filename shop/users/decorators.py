from django.shortcuts import redirect
from django.contrib import messages

def authenticated(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args,**kwargs)
        else:
            messages.info(request,'logout')
            return redirect('signin')
    return wrapper