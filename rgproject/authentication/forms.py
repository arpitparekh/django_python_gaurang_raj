from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  class Meta:  # inner class
    model = User
    fields =['username','first_name','last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
  pass


