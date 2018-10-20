from django.shortcuts import render, redirect
from .models import Raza, Estado, Mascota, Region, Ciudad, TipoVivienda
#Importamos la mensajeria de Django para usarla
from django.contrib import messages

#Un decorador nos permite extender la funcionalidad de un metodo. EN este caso particular le solicitaremos
#primero la utentificacion al usuario par aingresar a un View
from django.contrib.auth.decorators import login_required

# Create your views here.

#comentario
def home(request):
    return render(request, 'core/home.html')

def formulario(request):
    regiones = Region.objects.all() #Estas variables se
    ciudades = Ciudad.objects.all() #Estan haciendo
    tiposViviendas = TipoVivienda.objects.all()

    variables = {                   #Para
        'regiones':regiones,        #Llenar     
        'ciudades':ciudades,         #Los ComboBox, lo mismo con el formulario de mascotas
        'tiposViviendas':tiposViviendas
    }

    if request.POST:
        postulante = Postulante()
        postulante.correo = request.POST.get('txtCorreoElectronico')
        postulante.rut = request.POST.get('txtRut')
        postulante.nombreCompleto = request.POST.get('txtNombreCompleto')
        postulante.fechaNacimiento = request.POST.get('dateNacimiento')
        postulante.telefono = request.POST.get('txtTelefono')
        region = Region()
        region.id = request.POST.get('cboRegion')
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        tipoVivienda = TipoVivienda()
        tipoVivienda.id = request.POST.get('cboVivienda')

        try:
            postulante.save()
            variables['mensaje'] = 'Guardado Correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar correctamente'

    return render(request, 'core/formulario.html', variables)

def login(request):
    return render(request, 'core/login.html')

#CRUD DE MASCOTAS
@login_required #Con esto estamos protegiendo la URL de formulario_mascota
def formulario_mascota(request):
    
    razas = Raza.objects.all()  #Esta variable se hace para poder guardar todas las razas y asi poder sacar las que estan en la BBDD para un ComboBox
    estados = Estado.objects.all()

    variables = {
        'razas':razas,
        'estados':estados
    }

    if request.POST:
        mascota = Mascota()
        mascota.nombreMascota = request.POST.get('txtNombreMascota')
        mascota.genero = request.POST.get('txtGenero')
        mascota.fechaIngreso = request.POST.get('dateFechaIngreso')
        mascota.fechaNacimientoMascota = request.POST.get('dateFechaNacimiento')
        mascota.foto = request.POST.get('txtFoto')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza 

        try:
            mascota.save()
            variables['mensaje'] = 'Se ha guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar correctamente'


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

def modificar_mascota(request, id):
    #Buscamos la mascota para que se puedan modificar sus datos
    mascota = Mascota.objects.get(id=id)
    razas = Raza.objects.all()
    estados = Estados.objects.all()

    variables = {
        'mascota':mascota,
        'razas':razas,
        'estados':estados
    }

    if request.POST:
        mascota = Mascota()
        mascota.id = request.POST.get('txtId')
        mascota.nombreMascota = request.POST.get('txtNombreMascota')
        mascota.genero = request.POST.get('txtGenero')
        mascota.fechaIngreso = request.POST.get('dateFechaIngreso')
        mascota.fechaNacimientoMascota = request.POST.get('dateFechaNacimiento')
        mascota.foto = request.POST.get('txtFoto')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza 

    try:
        mascota.save()
        messages.success(request, 'Modificado correctamente')
    except:
        messages.error(request, 'No se ha podido modificar')
        return redirect('listado_mascotas') #Le estamos diciendo que si no se pudo modificar, que devuelva a la lista
    
    return render(request, 'core/modificar_mascota.html', variables )
