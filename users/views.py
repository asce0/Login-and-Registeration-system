from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'users/login.html')


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'users/logged_in.html')
    else:
        return render(request, 'users/register.html')

def log_out(request):
    logout(request)
    return render(request, 'users/login.html')
def register(request):
    return render(request, 'users/register.html')


def register_form(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    return render(request, 'users/login.html')
