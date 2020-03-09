from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def main_home(request) :
    return render(request, 'mainsite/main.html')

def user_page(request) :
    return render(request, "mainsite/manager.html")

def user_check(request) :
    username = request.POST.get("username")
    pwd = request.POST.get("password")
    user = authenticate(username=username, password=pwd)
    if user is not None:
        request.session['manager'] = user.username
        return redirect("home")
    else:
        return redirect("user_page")

def user_logout(request) :
    del request.session['manager']
    request.session.modified = True
    return redirect("home")