import email
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            return redirect('login_page')

    return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    return redirect('login_page')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            newUser = User.objects.create_user(username=username,email=None,password=password1)
            newUser.save()
            return redirect('login_page')

    return render(request,'register.html',{})



