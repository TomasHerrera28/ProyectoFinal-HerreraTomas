from django.shortcuts import render
from .models import Client
from AppTomas.forms import Client
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "AppTomas/index.html")

def products(request):
    return render(request, "AppTomas/products.html")

def contact(request):
    return render(request, "AppTomas/contact.html")

def contact_form(request):
    if request.method == "POST":
        mi_formulario = Client(request.POST) # Aqui me llega la informacion del html
        # print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Client(user=informacion["user"], email=informacion["email"], password=informacion["password"])

            cliente.save()
            return render(request, "AppTomas/index.html")
    else:
        mi_formulario = Client()

    return render(request, "AppTomas/contact_form.html", {"mi_formulario": mi_formulario})   
