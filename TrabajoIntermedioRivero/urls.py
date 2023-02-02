"""TrabajoIntermedioRivero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from AppIntermedia.views import*
from django.contrib.auth.views import LogoutView
from DM.views import (


    mensajes_privados


)

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('Formularios/DatosBancarios',Bancario,name="Bancario"),
    path('Formularios/DatosPersonales',Datos,name="Datos"),
    path('Buscar',Busqueda,name="Busqueda2"),
    path("Busqueda",Buscar,name="Buscar"),
    path("Busqueda1",Buscarpersona,name="Buscar1"),
    path("Busqueda0",buscar1,name="buscar0"),
    path("Inicio",inicio,name="Inix"),
    path("Formularios",Formularios,name="Formus"),
    path("Leertodo",leertodo,name="leerbanco"),
    path("verpaginas",verpaginas,name="ver"),
    path("Leertodo/<id>",borraruser,name="eliminar"),
    path("Leertodo1/<id>",borrarbanco,name="eliminar1"),
    path("Editar/<id>",editaruser,name="edit1"),
    path("EditarB/<id>",editarbanco,name="edit2"),
    path("Detalles",leerdetalle,name="detalle"),
    path("CrearUser",register,name="register"),
    path("agregarAvatar",agregarAvatar,name="agregarAvatar"),
    path("Login",loginseccion,name="loginseccion"),
    path("Logout",LogoutView.as_view(),name="logout"),
    path("About",About,name="About"),
    path('', include('DM.urls')),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
