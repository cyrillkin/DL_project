from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UsernameField, UserCreationForm
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.fields import DateField
from django.forms import fields, widgets
from django.forms.models import ModelForm

from root.models import Prof


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'placeholder': 'Имя пользователя',
        'class': 'form-input'
    }))

    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-input'
        })
    )

    error_messages = {
        'invalid_login': 'Введён неправильный логин или пароль'
    }


class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Пароли не совпадают'
    }
    
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'class': 'form-input'
        })
    )

    password2 = forms.CharField(
        label="Подтверждение пароля",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Подтвердите пароль',
            'class': 'form-input'
        }),
        help_text='Пароли не совпадают'
    )

    class Meta:
        model = User
        fields = ('email', 'username')
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': 'Электронная почта',
                'class': 'form-input'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Имя пользователя',
                'class': 'form-input'
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email должен быть уникальным')
        return email


class UpdateProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        label="Дата рождения",
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format=('%d-%m-%Y'), attrs={
            'class': 'form-control',
            'placeholder': 'Дата рождения в формате dd-mm-yyyy'
        })
    )

    class Meta:
        model = Prof
        fields = ['birth_date', 'avatar', 'city', 'description']
        labels = {
            'avatar': 'Фото',
            'city': 'Город',
            'description': 'Обо мне'
        }
