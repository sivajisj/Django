from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Register a new user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


#  Login form
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password1 = forms.CharField(widget=PasswordInput)



