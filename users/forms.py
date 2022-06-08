from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# to add a field on user creation form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # give nested namespace for conf and keep in same space
        model = User
        fields = ['username', 'email', 'password1', 'password2']
