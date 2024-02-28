import json
from typing import Dict, List

from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .models import Post, Username


# Домашняя страница
def home_page(request):
    with open('./first_app/static/news.json', encoding='utf8') as file:
        news: List[Dict[str, str]] = json.load(file)
    return render(request,
                  'home.html',
                  {'title': 'Главная', 'news': news, 'post': Post.objects.all()}
                  )


# Страница "О нас"
def about_page(request):
    with open('./first_app/static/about.json', encoding='utf8') as file:
        about: List[Dict[str, str]] = json.load(file)
    return render(request,
                  'about.html',
                  {'title': 'О НАС', 'about': about}
                  )


# Функция для создания формы на странице авторизации
def login_form(request):
    form = LoginForm(request.POST)
    return render(request, 'login_form.html', {'form': form})


# Функция для авторизации пользователя в приложении
def log_in(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        try:
            user = Username.objects.get(login=login, password=password)
            request.session['user_id'] = user.id
            user = request.user
            return render(request, 'user_page.html', {'user': user})
        except Username.DoesNotExist:
            message = 'Неверный логин или пароль!'
            return render(request, 'login_form.html', {'message': message})


# Функция выхода пользователя из приложения
def logout_user(request):
    logout(request)
    return redirect('login_form')


# Функция для регистрации пользователя в приложении
def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            Username.objects.create(login=login, password=password, email=email, name=name)
            return log_in(request)
    form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})


# Функция для восстановления пароля пользователя
def forgot_password(request):
    return render(request, 'forgot_password.html')
