from django.db import models

# Create your models here.
class Navbar(models.Model):
	id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
	nombre = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

class Contacto(models.Model):
	id_contacto = models.AutoField(db_column="idContacto", primary_key=True)
	nombre = models.CharField(max_length=100)
	correo = models.CharField(max_length=100)
	asunto = models.CharField(max_length=100)
	mensaje = models.CharField(max_length=255)

def __str__(self):
    return self.nombre
	
