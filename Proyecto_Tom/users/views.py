from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from users.models import Avatar

def login_request(request):
    msg_login = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppTomas/index.html")
            
        msg_login = "Usuario o contraseña incorrectos"
    
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):
    
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"AppTomas/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/register.html" ,  {"form":form, "msg_register": msg_register})

@login_required
def edit_user(request):
    
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, request.FILES, instance=usuario)
         
        if formulario.is_valid():
            
            if formulario.cleaned_data.get("imagen"):
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data.get("imagen"))
                avatar.save()
                
            formulario.save()
            return render(request, "AppTomas/index.html")
    else:
        formulario = UserEditForm(instance=usuario)
            
        return render(request, "users/edit_user.html", {"form": formulario})
            
            
class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/change_password.html"
    success_url = reverse_lazy('EditUser')