from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib import messages
# Create your views here.

@login_required(login_url='login_page')
def home_view(request):
    #tworzenie posta 
    if request.method == 'POST':
        tytul = request.POST['tytul']
        zawartosc=request.POST['zawartosc']

        if len(tytul)>2 and len(zawartosc)>2:
            nowypost = Post(tytul=tytul,autor=request.user,zawartosc=zawartosc)
            nowypost.save()
        else:
            messages.error(request,'Is to short')

    #wyswietlanie wszytkich postów w homepage 
    posty=Post.objects.all()
    post_wyswietlanie={
        'posty':posty
    }
    return render(request,'home.html',post_wyswietlanie)

def profil_page(request):
    posty=Post.objects.filter(autor=request.user)
    
    post_wyswietlanie={
        'posty':posty
    }
    return render(request,'profil.html',post_wyswietlanie)