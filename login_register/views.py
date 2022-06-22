from curses.ascii import isdigit
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import *


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


@login_required(login_url='login_page')
def logout_user(request):
    logout(request)
    return redirect('login_page')

def register_user(request):
    error_list=[]
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if isdigit(username[0]):
            error_list.append('The first character must be a letter')
        if len(username)<2:
            error_list.append('Username is to short')
        if len(password1)<6:
            error_list.append('Password is to short')
        if password1 != password2:
            error_list.append('Passwords are not the same')
        if len(error_list)==0:
            try:
                newUser = User.objects.create_user(username=username,email=None,password=password1)
                newUser.save()
                return redirect('login_page')
            except:
                messages.error(request,'Username already exists')

    errory = {
        'lista':error_list
    }

            

    return render(request,'register.html',errory)



