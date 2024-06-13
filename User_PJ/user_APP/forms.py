from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  #эти два импорта связанны с юзером в базе данных


class UserAuthForm(UserCreationForm):  #форма регистрации
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(forms.Form):  #форма входа
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control' ,
                                                                                 'placeholder': 'Password'}
                                                                            ))
