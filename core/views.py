from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


@login_required(login_url='/login/')
def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)


def login_user(request):
    template_name = 'core/login.html'
    return render(request, template_name)


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Usuarios e senha inválidos.")

    return redirect('/login/')


def logout_user(request):
    logout(request)
    return redirect('/login/')