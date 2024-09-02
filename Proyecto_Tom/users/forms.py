from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}
        
class UserEditForm(UserChangeForm):
    password = None
    firts_name = forms.CharField(label="Name:")
    last_name = forms.CharField(label="Last name:")
    email = forms.EmailField(label="Email:")
    imagen = forms.ImageField(label="Avatar", required=False)
   
    class Meta:
        model = User
        fields = ["firts_name", "last_name", "email", "imagen"]