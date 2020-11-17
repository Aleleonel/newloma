

from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


def login_user(request):
    template_name = 'core/login.html'
    return render(request, template_name)


@csrf_protect
def login_submit(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login/#')
        else:
            messages.error(request, "Usuário inválidos, por favor tente novamente!")
    return redirect('/login/')