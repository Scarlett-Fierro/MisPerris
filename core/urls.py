from django.urls import path
from .views import home, formulario, login, listar_mascotas, eliminar_mascota, formulario_mascota, modificar_mascota, get_ciudades #Estamos importando la funcion "home" y la funcion "formulario " que hicimos en views

urlpatterns = [
    path('', home, name="home"), # Al principio no le pusimos ruta ya que se vera solo al poner la raiz que seria localhost
    path('formulario/', formulario, name="formulario"), # aqui le estamos diciendo que cuando le agregamos el /formulario nos va a llamar la funcion formulario que hicimos en views y el name sirve para llamarlo desde otro lado
    path('login/', login, name="login"),
    path('listar-mascotas/', listar_mascotas, name="listado_mascotas"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('formulario-mascota/', formulario_mascota, name="formulario_mascota"),
    path('modificar-mascota/<id>/', modificar_mascota, name="modificar_mascota"),
    path('get_ciudades/<id>/', get_ciudades, name="get_ciudades"),
]