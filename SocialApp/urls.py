"""SocialApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login_register import views as login_register_views
from main_home import views as main_home_views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',login_register_views.login_user,name='login_page'),
    path('logout/',login_register_views.logout_user,name='logout_page'),
    path('register/',login_register_views.register_user,name='register_page'),
    
    path('',main_home_views.home_view,name='home_page'),
    path('profil/',main_home_views.profil_page,name='profil_page'),
    
]
