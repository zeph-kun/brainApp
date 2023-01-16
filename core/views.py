from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Users, Catalogue


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


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        passwd1 = request.POST.get('password1')
        passwd2 = request.POST.get('password2')

        if passwd1 != passwd2:
            messages.error(request, 'Les mots de passes ne match pas')
            return redirect('register')

        if Users.object.filter(email=email).exists():
            messages.error(request, 'Email déjà utilisé')
            return redirect('register')

        user = Users.object.create_user(email=email, first_name=first_name, last_name=last_name, password=passwd1)
        user.save()
        login(request, user)
        messages.success(request, f'Account created for {first_name}!')
        return redirect('index')

    return render(request, "register.html")


def catalog(request):
    data = Catalogue.objects.all()
    context = {
        'data': data
    }
    return render(request, "catalog.html", context=context)
