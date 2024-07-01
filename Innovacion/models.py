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

class Afiliado(models.Model):
	id_afiliado = models.AutoField(db_column="idAfiliado", primary_key=True)
	nombre_afiliado = models.CharField(max_length=60)
	rubro = models.CharField(max_length=50)
	monto_acelerado = models.IntegerField(null= False)

	
