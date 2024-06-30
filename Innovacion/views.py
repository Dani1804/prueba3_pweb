from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    Navbars = Navbar.objects.all()
    context = {
        "Navbars": Navbars
    }
    return render(request, 'Innovacion/home.html', context)

def quienesSomos(request):
    Navbars = Navbar.objects.all()
    context = {
        "Navbars": Navbars
    }
    return render(request, 'Innovacion/quienesSomos.html', context)

def servicios(request):
    Navbars = Navbar.objects.all()
    context = {
        "Navbars": Navbars
    }
    return render(request, 'Innovacion/servicios.html', context)