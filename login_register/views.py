from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import User_creation

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
    form = User_creation()
    if request.method == 'POST':
        form = User_creation(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            if user is not None:
                login(request,user)
                return redirect('home_page')

    return render(request,'register.html',{'forma_register':form})


