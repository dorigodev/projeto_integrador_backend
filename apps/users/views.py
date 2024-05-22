from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from apps.users.forms import LoginForm
from apps.users.forms import RegisterForm


# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = form['nome_login'].value()
            password = form['senha_login'].value()
            user = authenticate(username=user_login, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Loja logada com sucesso!')
                return redirect("index")
            else:
                messages.error(request, 'Erro ao logar com sucesso!')
                return redirect("login")
    return render(request, 'users_templates/login.html', {'form': form})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_login_register = form['nome_registro'].value()
            password = form['senha_registro'].value()
            email = form['email'].value()
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Usuário já cadastrado')
                return redirect("register")
            new_user = User.objects.create_user(
                username=user_login_register,
                email=email,
                password=password)
            new_user.save()
            messages.success(request, f'{login} registrado com sucesso!')
            return redirect('login')
    return render(request, 'users_templates/register.html', {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect("login")
