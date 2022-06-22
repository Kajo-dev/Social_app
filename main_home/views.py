from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.

@login_required(login_url='login_page')
def home_view(request):

    posty=Post.objects.all()


    post_wyswietlanie={
        'posty':posty
    }
    return render(request,'home.html',post_wyswietlanie)