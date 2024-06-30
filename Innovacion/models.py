from django.db import models

# Create your models here.
class Navbar(models.Model):
	id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
	nombre = models.CharField(max_length=50)
	url = models.CharField(max_length=100)
	
