import json
from typing import Dict, List

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Post, Username


def home_page(request):
    with open('./first_app/static/news.json', encoding='utf8') as file:
        news: List[Dict[str, str]] = json.load(file)
    return render(request,
                  'home.html',
                  {'title': 'Главная', 'news': news, 'post': Post.objects.all()}
                  )


def about_page(request):
    with open('./first_app/static/about.json', encoding='utf8') as file:
        about: List[Dict[str, str]] = json.load(file)
    return render(request,
                  'about.html',
                  {'title': 'О НАС', 'about': about}
                  )


def login_form(request):
    form = LoginForm(request.POST)
    return render(request, 'login_form.html', {'form': form})


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


def logout_user(request):
    logout(request)
    return redirect('login_form')


def registration_user(request):
    return render(request, 'registered_page.html')
