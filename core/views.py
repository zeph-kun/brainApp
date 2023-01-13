from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def index(request):
    return render(request, "index.html")


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        messages.error(request, 'Email or password is incorrect')
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('login')

