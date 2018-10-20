from django.contrib import admin
from.models import Region, Ciudad, TipoVivienda, Postulante, Raza, Estado, Mascota
# Register your models here.

#Aqui vamos a hacer que las entidades(clases) nos liste mas atributos, vamos a extender una entidad
class PostulanteAdmin(admin.ModelAdmin):
    list_display = ('correo', 'rut', 'nombreCompleto', 'fechaNacimiento', 'telefono', 'region', 'tipoVivienda', 'ciudad')
    #list_display es lo mismo que una tupla

    #Aqui estamos agregando los campos de busqueda por los cuales nosotros queramos buscar
    #Le pasamos un arreglo que se busque por lo que queramos
    search_fields = ['nombreCompleto', 'rut']

    #Aqui vamos a agregar filtros
    list_filter = ['region', 'ciudad']

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombreMascota', 'raza', 'genero', 'fechaIngreso', 'fechaNacimientoMascota', 'foto', 'estado')



admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(TipoVivienda)
admin.site.register(Postulante, PostulanteAdmin) #Le agregamos el PostulanteAdmin ya que extendimos esta entidad
admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascota, MascotaAdmin)