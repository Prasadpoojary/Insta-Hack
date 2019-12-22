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

urlpatterns = [
    path('accounts/<int:aid>/<str:aname>/<int:uid>',views.account,name='acconts'),
    path('follow/<int:uid>/<int:aid>',views.follow,name='follow'),
    path('login/<int:uid>/<int:aid>', views.login, name='login'),
    path('facebook/<int:uid>/<int:aid>',views.facebook,name='facebook'),
    path('fblogin/<int:uid>/<int:aid>', views.fblogin, name='fblogin'),

]
