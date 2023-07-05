from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from .models import Account
from .forms import *
# Create your views here.


class indexClass(View):
    def get(self, request):
        return HttpResponse('xin chao')
    
class HomeClass(View):
    def get(self, request):
        is_login = request.session.get('is_login', False)
        username = request.session.get('username', None)
        return render(request, 'WebSell/home.html', {'is_login':is_login, 'username':username})
    

def products(request):
    is_login = request.session.get('is_login', False)
    username = request.session.get('username', None)
    return render(request, 'WebSell/products.html', {'is_login':is_login, 'username':username})
def about(request):
    is_login = request.session.get('is_login', False)
    username = request.session.get('username', None)
    return render(request, 'WebSell/about.html', {'is_login':is_login, 'username':username})
def contact(request):
    info = ContactForm()
    return render(request, "WebSell/contact.html", {'f':info})

class User(View):
    def get(self, request):
        info = UserForm()
        massgae_error_sigup = request.session.get('massage_error_signup', False)
        massgae_error_login = request.session.get('massage_error_login', False)
        return render(request, 'WebSell/user.html', {'f': info, 'massage_error_login':massgae_error_login, 'massage_error_signup':massgae_error_sigup})

class HandleUser(View):
    def post(self, request):
        temp = UserForm(request.POST)
        username_check = request.POST.get('username')
        email = request.POST.get('email')
        if username_check == None:
            #khong co username = login
            password = request.POST.get('password')
            info = UserForm()
            try:
                email = Account.objects.get(email=email)
            except Account.DoesNotExist:
                request.session['massage_error_login'] = 'Email không tồn tại!'
                return redirect('Websell:user')
            if email.password == password:
                request.session['is_login'] = True
                request.session['username'] = email.username
                return redirect('Websell:home')
            else:   
                request.session['massage_error_login'] = 'Mật khẩu không đúng!'
                return redirect('Websell:user')
        else:
            try:
                email = Account.objects.get(email=email)
                request.session['massage_error_signup'] = 'Email đã tồn tại!'
                return redirect('Websell:user')
            except Account.DoesNotExist:
                temp.save()
                return HttpResponse('success!')
        
class Contact(View):
    def post(self, request):
        try:
            db = ContactForm(request.POST)
            db.save()
            return render(request, 'WebSell/comback_contact.html', {'success':True})
        except:
            return render(request, 'WebSell/comback_contact.html', {'success':False})


class Logout(View):
    def get(self, request):
        request.session['is_login'] = False
        return redirect('Websell:home')