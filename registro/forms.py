from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario

class CreateUser(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=100)
    email = forms.EmailField(label="E-mail")