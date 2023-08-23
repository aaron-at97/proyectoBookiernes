from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import (
    ModelForm, TextInput, EmailInput, CharField, EmailField, PasswordInput, Select
)
from django import forms

from eBook.models import Book


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={
        'class':'form-control input-md input-with-feedback',
        'id': 'usuari',
        'style': 'min-width: 0; width: 35%; margin: 2% 0; display: inline;',
        'placeholder' : 'Usuario',
    }), required=True)

    password = forms.CharField(widget=PasswordInput(attrs={
        'class':'form-control input-md',
        'id': 'password',
        'style': 'min-width: 0; width: 35%; margin: 2% 0; display: inline;',
        'placeholder': 'Contraseña',
    }), required=True)

    class Meta:
        model = User

    fields = [
        'username',
        'password',
    ]


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['id_book',
                  'title',
                  'genere',
                  'body',
                  ]

    id_book = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ISBN',}),label='')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titulo',}),label='')
    genere = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Genero',}),label='')
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descripcion',}),label='')