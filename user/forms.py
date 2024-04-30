from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'phone_number', 'password1')


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form=control', 'placeholder': 'Добавьте Почту'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form=control', 'placeholder': 'Напишите Почту'}))


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'phone_number')