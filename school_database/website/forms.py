from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
   
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    nationality = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    mobile = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'country', 'nationality', 'mobile', 'admin', 'student', 'staff','editor')
