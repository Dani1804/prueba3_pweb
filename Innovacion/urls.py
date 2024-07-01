from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('quienes-somos', views.quienesSomos, name='quienes-somos'),
    path('servicios', views.servicios, name='servicios'),
    path('contacto', views.contacto, name='contacto'),
    path('success', views.success, name='success')
]