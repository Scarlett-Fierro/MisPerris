from django.shortcuts import render, redirect
from .models import Raza, Estado, Mascota
#Importamos la mensajeria de Django para usarla
from django.contrib import messages

#Un decorador nos permite extender la funcionalidad de un metodo. EN este caso particular le solicitaremos
#primero la utentificacion al usuario par aingresar a un View
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def login(request):
    return render(request, 'core/login.html')

#CRUD DE MASCOTAS
@login_required #Con esto estamos protegiendo la URL de formulario_mascota
def formulario_mascota(request):
    
    razas = Raza.objects.all()  #Esta variable se hace para poder guardar todas las razas y asi poder sacar las que estan en la BBDD para un ComboBox
    variables = {
        'razas':razas
    }

    # estados = Estado  NO SE PORQUE PUSE ESTO

    if request.POST:
        mascota = Mascota()
        mascota.nombreMascota = request.POST.get('txtNombreMascota')
        mascota.genero = request.POST.get('txtGenero')
        mascota.fechaIngreso = request.POST.get('dateFechaIngreso')
        mascota.fechaNacimientoMascota = request.POST.get('dateFechaNacimiento')
        
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza 


    return render(request, 'core/formulario_mascota.html', variables)

def listar_mascotas(request):
    
    mascotas = Mascota.objects.all() #Aquí hicimos una variable mascotas que almacena a todas las mascotas

    return render(request, 'core/listar_mascotas.html', { #Aqui en vez de pasar solo la variable, la hacemos un diccionario para que despues no tengamos problemas
    #en caso de querer pasar otra variable 
        'mascotas':mascotas
    })

def eliminar_mascota(request, id):
    #Buscar la mascota que queremos eliminar
    mascota = Mascota.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar esta mascota"
        messages.error(request, mensaje)

    return redirect('listado_mascotas') #El redirect esta diciendo que el mensaje lo va a recibir el listado_automoviles


