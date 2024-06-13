from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from user_APP.forms import UserAuthForm, SignInForm


# Create your views here.

def register(request):  # функция регистрации на сайте
    if request.user.is_authenticated:
        return redirect('profile_page')
    if request.method == 'POST':
        form = UserAuthForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
            # регистрация юзера
    form = UserAuthForm()
    return render(request, 'user_APP/register.html', {'form': form})


def login_view(request):  # функция входа на сайте
    if request.user.is_authenticated:
        return redirect('profile_page')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)  # проверка пароля и логина
            if user is not None:  # проверка найден ли пользователь в бд
                login(request, user)
                return redirect('profile_page')
            else:
                print('User not found')
    form = SignInForm()
    ctx = {
        'form': form
    }
    return render(request, 'user_APP/Login.html', ctx)


def profile_view(request):
    if not request.user.is_authenticated:  # проверка авторизован ли юзер
        return redirect('login')
    ctx = {
        'user': request.user
    }
    return render(request, 'user_APP/profile.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('login')