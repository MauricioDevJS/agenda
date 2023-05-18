from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = auth.authenticate(username=username, password=password)
      
        if check_user == None:
            return redirect('login')
        else:
            auth.login(request, check_user)
            return redirect('home')
    else:
        return render(request, 'pages/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):

    if request.method == 'POST':
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('repassword')

        User.objects.create_user(username=nome, password=senha, email=email)
        return redirect('login')
    else:
        return render(request, 'pages/cadastro.html')