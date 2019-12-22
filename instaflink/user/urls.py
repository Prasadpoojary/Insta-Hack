"""instaflink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('login', views.login, name='login'),
    path('logme', views.logme, name='logme'),
    path('register',views.register,name='register'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('home', views.logme, name='logme'),
    path('forgot', views.forgot, name='forgot'),
    path('getpass', views.getpass, name='getpass'),
    path('create', views.create, name='create'),
    path('homepage', views.homepage, name='homepage'),
    path('profile', views.profile, name='profile'),
    path('feadback', views.feadback, name='feadback'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('delete<int:id>',views.delete,name='delete'),
    path('edit', views.edit, name='edit'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('feadit', views.feadit, name='feadit'),
    path('logout',views.logout,name='logout')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
