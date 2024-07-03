from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    Navbars = Navbar.objects.all()
    context = {
        "Navbars": Navbars
    }
    return render(request, 'Innovacion/home.html', context)

def quienesSomos(request):
    Navbars = Navbar.objects.all()
    Afiliados = Afiliado.objects.all()
    context = {
        "Navbars": Navbars,
        "Afiliados":Afiliados
    }
    return render(request, 'Innovacion/quienesSomos.html', context)

def servicios(request):
    Navbars = Navbar.objects.all()
    Servicios = Servicio.objects.all()
    context = {
        "Navbars": Navbars,
        "Servicios": Servicios
    }
    return render(request, 'Innovacion/servicios.html', context)


def contacto(request):
    Navbars = Navbar.objects.all()
    context = {
        "Navbars": Navbars
    }
    if request.method == 'POST':
        form = contactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = contactoForm()
    
    # Combina ambos diccionarios en uno solo
    context.update({'form': form})
    return render(request, 'Innovacion/contacto.html', context)


def success(request):
    Navbars = Navbar.objects.all()
    context = {
        "Navbars": Navbars
    }
    return render(request, 'Innovacion/success.html', context)

