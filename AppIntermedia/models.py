from django.db import models
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Banco(models.Model):
    Nombre=models.CharField(max_length=30)
    Pais=models.CharField(max_length=30)
    Provincia=models.CharField(max_length=20)
    Cuenta=models.IntegerField()
    Sucursal=models.CharField(max_length=20)


    def __str__(self):
        return self.Nombre+" "+str(self.Pais)

class Identidad(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Edad=models.IntegerField()
    Pais=models.CharField(max_length=50)
    Provincia=models.CharField(max_length=50)
    Localidad=models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre+" "+str(self.Apellido)


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.user} - {self.imagen}"
