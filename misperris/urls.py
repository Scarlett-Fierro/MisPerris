"""misperris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include ('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]

#Personalizacion de los titulos del administrador

#Con esto estamos cambiando el titulo del Header
admin.site.site_header = "Administracion de Mis Perris"

#Con esto estamos cambiando la primera parte del titulo de la pestaña y el tambien el primer titulo debajo del Header
admin.site.index_title = "Mis Perris"

#Con esto estamos cambiando la segunda parte del titulo de la pestaña
admin.site.site_title = "Administracion Mis Perris"