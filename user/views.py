from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import re
from chat.models import Buttonhits
# Create your views here.
def home(request):
    button_hits = Buttonhits.objects.all()
    return render(request, 'home.html',{"button_hits":button_hits})

def user_register(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2'] 
        # Check if password's match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                else:
                    user = User.objects.create_user(first_name=first_name, username=username, password=password, 
                    email=email, last_name=last_name)
                    user.save()
                    messages.success(request, 'Registered successfully...')
                    return redirect('login')
          
        else:
            messages.error(request, 'Passwords do not match')
    else:
        form = CreateUserForm()
    return render(request, 'register.html',{'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # To check whether user input is Mail id or Username
        if(re.search("@gmail.com$", email)):
            user_list = User.objects.filter(email=email)
            for val in user_list:
                user = authenticate(request, username=val.username, password=password)
        else:
            user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully...")
    return redirect('home')