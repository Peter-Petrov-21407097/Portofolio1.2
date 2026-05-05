from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class MagicLinkForm(forms.Form):
    email = forms.EmailField(label="Email")