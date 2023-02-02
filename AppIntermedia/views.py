from django.shortcuts import render
from AppIntermedia.forms import*
from AppIntermedia.models import Banco,Identidad,Avatar
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def avatardef(request):
    avatar1=Avatar.objects.filter(user=request.user)
    if len(avatar1)!= 0:
        avatar=avatar1[0].imagen.url
    else:
        avatar=""
    
    return avatar

@login_required
def Bancario(request):
    if request.method == "POST":

        formulario=Bank(request.POST)

        if formulario.is_valid():
            informacion=formulario.cleaned_data
            nombre=request.POST["Nombre"]
            pais=request.POST["Pais"]
            provincia=request.POST["Provincia"]
            cuenta=request.POST["Cuenta"]
            sucursal=request.POST["Sucursal"]
            clase=Banco(Nombre=nombre, Pais=pais,Provincia=provincia,Cuenta=cuenta,Sucursal=sucursal)
            clase.save()
            return render (request,"template.html",{"formulario":formulario})

    else:

        formulario=Bank()
        return render(request,"template.html", {"formulario":formulario})

@login_required
def Datos(request):
    if request.method == "POST":
        formula=Ident(request.POST)
        
        if formula.is_valid():
            info=formula.cleaned_data
            nombre=request.POST["Nombre"]
            apellido=request.POST["Apellido"]
            edad=request.POST["Edad"]
            pais=request.POST["Pais"]
            localidad=request.POST["Localidad"]
            provincia=request.POST["Provincia"]
            clase=Identidad(Nombre=nombre,Apellido=apellido,Edad=edad,Pais=pais,Localidad=localidad,Provincia=provincia)
            clase.save()
            return render (request,"DatosPersonales.html",{"form":formula})
    
    
    else:
        formula=Ident()
        return render(request,"DatosPersonales.html",{"form":formula,"mensaje2":"Error! No se pudo Guardar los Datos"})

@login_required
def Busqueda(request):
    return render(request,"Busqueda.html")

@login_required
def Buscar(request):

    banco0= request.GET['Banco']

    if banco0 !="":
       var=Banco.objects.filter(Nombre=banco0)
       return render(request,"Resultados.html",{"var":var})
        
    else:
        return render(request,"Busqueda.html")    


@login_required
def buscar1(request):
    return render(request,"BuscarDatos.html")

@login_required
def Buscarpersona(request):

    Identida= request.GET['Nombre']

    if Identida !="":
       var0=Identidad.objects.filter(Nombre=Identida)
       return render(request,"BusquedaIdent.html",{"var0":var0})

    else:
        return render(request,"BuscarDatos.html")



def inicio(request):
    try:

        avatar1=Avatar.objects.filter(user=request.user)
        if len(avatar1)!= 0:
           avatar=avatar1[0].imagen.url
    
    
        else:
            avatar=""
        return render(request,"C:\TrabajoIntermedio--rivero-main\AppIntermedia\Plantillas\index.html",{"avatar":avatar})
    except:
    
        return render(request,"C:\TrabajoIntermedio--rivero-main\AppIntermedia\Plantillas\index.html")


@login_required
def Formularios(request):
    return render(request,"Formularios.html",{"avatar":avatardef(request)})



def About(request):
    return render(request,"About.html",{"avatar":avatardef(request)})



def leertodo(request):

    banco = Banco.objects.all()
    ident = Identidad.objects.all()
    context = {"bancos":banco,"ident":ident}
    return render(request,"leertodo.html",context)

@login_required
def leerdetalle(request):

    banco = Banco.objects.all()
    ident = Identidad.objects.all()
    context = {"bancos":banco,"ident":ident}
    return render(request,"detalladoleer.html",context)



def verpaginas(request):
    return render (request,"verpaginas.html")



@login_required
def borraruser(request, id):

    user=Identidad.objects.get(id=id)
    user.delete()
    banco = Banco.objects.all()
    ident = Identidad.objects.all()
    context = {"bancos":banco,"ident":ident,"mensaje1":"El Usuario Fue Eliminado Correctamente!"}
    return render (request,"leertodo.html",context)

@login_required
def borrarbanco(request, id):    
    user= Banco.objects.get(id=id)
    user.delete()
    banco = Banco.objects.all()
    ident = Identidad.objects.all()
    context = {"bancos":banco,"ident":ident,"mensaje":"El Banco Fue Eliminado Correctamente!"}
    return render(request,"leertodo.html",context)


@login_required
def editaruser(request,id):
    user=Identidad.objects.get(id=id)
    if request.method=="POST":
        form= Ident(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user.Nombre=info["Nombre"]
            user.Apellido=info["Apellido"]
            user.Edad=info["Edad"]
            user.Pais=info["Pais"]
            user.Localidad=info["Localidad"]
            user.Provincia=info["Provincia"]
            user.save()
            banco = Banco.objects.all()
            ident = Identidad.objects.all()
            context = {"bancos":banco,"ident":ident,"mensaje1":"El Usuario Fue Editado Correctamente!"}
            return render(request,"leertodo.html",context)

    else:
        user=Identidad.objects.get(id=id)
        formulario=Ident(initial={"Nombre":user.Nombre,
        "Apellido":user.Apellido,"Edad":user.Edad,
        "Pais":user.Pais,"Localidad":user.Localidad,
        "Provincia":user.Provincia})
        return render(request,"editaruser.html",{"form":formulario,"user":user})   
        

@login_required
def editarbanco(request,id):
    user=Banco.objects.get(id=id)
    if request.method=="POST":
        form= Bank(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user.Nombre=info["Nombre"]
            user.Pais=info["Pais"]
            user.save()
            banco = Banco.objects.all()
            ident = Identidad.objects.all()
            context = {"bancos":banco,"ident":ident,"mensaje":"El Banco Fue Editado Correctamente!"}
            return render(request,"leertodo.html",context)

    else:
        user=Banco.objects.get(id=id)
        formulario=Bank(initial={"Nombre":user.Nombre,
        "Pais":user.Pais})
        return render(request,"editarbanco.html",{"form":formulario,"user":user})   
        


def register(request):
    if request.method == "POST":
        form= RegisterUser(request.POST)
        if form.is_valid():
            user= form.cleaned_data.get("username")
            form.save()
            return render(request,"index.html",{"mensaje":f"Usuario {user} Fue Creado Correctamente"})

        else:
            return render(request,"register.html",{"mensaje":"Error!! El Usuario no se Pudo Crear, Intentalo Nuevamente!","form":form})
    
    
    else:
        form= RegisterUser()
        return render(request,"register.html",{"form":form})



def loginseccion(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user=info["username"]
            clave=info["password"]
            usuario=authenticate(username=user,password=clave)
            if usuario is not None:
                login(request,usuario)
                return render(request,"index.html")

            else:
                return render(request,"login.html",{"form":form,"mensaje":"Usuario o Contraseña Incorrectos"}) 
    
        else:
            return render(request,"login.html",{"form":form,"mensaje":"Usuario o Contraseña Incorrectos"})

    else:
        form=AuthenticationForm()
        return render(request,"login.html",{"form":form,})



def agregarAvatar(request):
    if request.method == "POST":
        form=AvatarForm(request.POST,request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar0=Avatar.objects.filter(user=request.user)
            if len(avatar0)> 0:
                avatar0[0].delete()
            avatar.save()
            return render (request,"index.html",{"mensaje":f"Avatar agregado al Usuario:{request.user}"})
        else:
            return render (request,"avatarform.html",{"form":form,"usuario":request.user,"mensaje":"Error al cargar la imagen"})
    else:
        form=AvatarForm()
        return render(request,"avatarform.html",{"form":form,"usuario":request.user})

