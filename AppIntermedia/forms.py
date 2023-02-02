from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Bank(forms.Form):
    Nombre=forms.CharField(label="Nombre Del Banco",max_length=20)
    Pais=forms.CharField(label="Pais Del Banco",max_length=20)
    Provincia=forms.CharField(label="Provincia Del Banco",max_length=20)
    Cuenta=forms.IntegerField(label="Numero de Cuenta Del Banco")
    Sucursal=forms.CharField(label=" N° Sucursal Del Banco",max_length=20)

class Ident(forms.Form):
    Nombre=forms.CharField(label="Nombre",max_length=50)
    Apellido=forms.CharField(label="Apellido",max_length=50)
    Edad=forms.IntegerField(label="Edad")
    Pais=forms.CharField(label="Pais",max_length=50)
    Localidad=forms.CharField(label="Localidad",max_length=50)
    Provincia=forms.CharField(label="Provincia",max_length=50)

   
class RegisterUser(UserCreationForm):
      
      email=forms.EmailField(label="Email")
      password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
      password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
      
      class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts={k:"" for k in fields}



class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")