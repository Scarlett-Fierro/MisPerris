from django.contrib import admin
from.models import Region, Ciudad, TipoVivienda, Postulante, Raza, Estado, Mascota, Genero
# Register your models here.

#Aqui vamos a hacer que las entidades(clases) nos liste mas atributos, vamos a extender una entidad
class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'rut', 'nombreCompleto', 'fechaNacimiento', 'telefono', 'region', 'tipoVivienda', 'ciudad')
    #list_display es lo mismo que una tupla

    #Aqui estamos agregando los campos de busqueda por los cuales nosotros queramos buscar
    #Le pasamos un arreglo que se busque por lo que queramos
    search_fields = ['nombreCompleto', 'rut']

    #Aqui vamos a agregar filtros
    list_filter = ['region', 'ciudad']

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreMascota', 'raza', 'genero', 'fechaIngreso', 'fechaNacimientoMascota', 'foto', 'estado')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreRegion')

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreCiudad', 'region')

class TipoViviendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreVivienda')

class RazaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreRaza')

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreEstado')

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreGenero')



admin.site.register(Region, RegionAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(TipoVivienda, TipoViviendaAdmin)
admin.site.register(Postulante, PostulanteAdmin) #Le agregamos el PostulanteAdmin ya que extendimos esta entidad
admin.site.register(Raza, RazaAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Mascota, MascotaAdmin)