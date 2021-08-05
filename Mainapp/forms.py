from django import forms
from django.core import validators
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class LoginForm (forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'id': 'id_username1'
                }
            )
        )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput()
        )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']  

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos introducidos son erroneos')
            


class UpdatePasswordsForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña Actual',
        widget=forms.PasswordInput(
            attrs={
                'id': 'id_username1',
                'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contraseña Nueva',
        widget=forms.PasswordInput(
            attrs={
                'id': 'id_username1',
                'placeholder':'Contraseña'
            }
        )
    )
