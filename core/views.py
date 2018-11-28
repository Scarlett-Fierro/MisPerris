from django.shortcuts import render, redirect
from .models import Raza, Estado, Mascota, Region, Ciudad, TipoVivienda, Genero, Postulante
#Importamos la mensajeria de Django para usarla
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

#Un decorador nos permite extender la funcionalidad de un metodo. EN este caso particular le solicitaremos
#primero la utentificacion al usuario par aingresar a un View
from django.contrib.auth.decorators import login_required
from fcm_django.models import FCMDevice

# Create your views here.

#comentario
def home(request):
    #Hacemos una variable mascota que almacene todas las mascota, esto lo hacemos para la galeria
    mascotasSlider = Mascota.objects.filter(estado_id=3) #El id 3 es de los perros adoptados
    mascotasGaleria = Mascota.objects.filter(estado_id=2) #El id 2 es de los perros rescatados
    #Hicimos un diccionario para guardar todas las mascotas

    variables = {
        'mascotasSlider': mascotasSlider,
        'mascotasGaleria': mascotasGaleria,
    }

    return render(request, 'core/home.html', variables)

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
        postulante.region = region
        postulante.ciudad = ciudad
        postulante.tipoVivienda = tipoVivienda

        
        try:
            postulante.save()
            variables['mensaje'] = 'El postulante ' "'"+postulante.nombreCompleto+"'" ' se ha guardado correctamente'
        except:
            variables['mensaje'] = 'El postulante ' "'"+postulante.nombreCompleto+"'" ' no se ha podido guardar correctamente'

    return render(request, 'core/formulario.html', variables)

def login(request):
    return render(request, 'core/login.html')

#CRUD DE MASCOTAS
@login_required #Con esto estamos protegiendo la URL de formulario_mascota
@permission_required('Mascota.puede_agregar')
def formulario_mascota(request):

    razas = Raza.objects.all()  #Esta variable se hace para poder guardar todas las razas y asi poder sacar las que estan en la BBDD para un ComboBox
    estados = Estado.objects.all()
    generos = Genero.objects.all()

    variables = {
        'razas':razas,
        'estados':estados,
        'generos':generos
    }

    if request.POST:
        mascota = Mascota()
        mascota.nombreMascota = request.POST.get('txtNombreMascota')
        mascota.fechaIngreso = request.POST.get('dateFechaIngreso')
        mascota.fechaNacimientoMascota = request.POST.get('dateFechaNacimientoMascota')
        mascota.foto = request.FILES.get('fileFoto')
        estado = Estado()
        estado.id = request.POST.get('cboEstado')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        genero = Genero()
        genero.id = request.POST.get('cboGenero')
        mascota.raza = raza 
        mascota.estado = estado
        mascota.genero = genero

        
        try:
            mascota.save()
            #Obtenemos todos los dispositivos con el Token
            dispositivos = FCMDevice.objects.all()
            #A cada dispositivo se le envia una notificacion
            dispositivos.send_message(
                title="Alerta MisPerris",
                body="Se ha agregado una nueva mascota",
                icon="/static/core/img/logoAplicacion.png"
            )

            variables['mensaje'] = 'La mascota ' "'"+mascota.nombreMascota+"'" ' se ha guardado correctamente'
        except:
            variables['mensaje'] = 'La mascota ' "'"+mascota.nombreMascota+"'" ' No se ha podido guardar correctamente'


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
        mensaje = 'La mascota ' "'"+mascota.nombreMascota+"'" ' se ha eliminado correctamente'
        messages.success(request, mensaje)
    except:
        mensaje = 'La mascota ' "'"+mascota.nombreMascota+"'" ' no se ha podido eliminar'
        messages.error(request, mensaje)

    return redirect('listado_mascotas') #El redirect esta diciendo que el mensaje lo va a recibir el listado_mascotas

def modificar_mascota(request, id):
    #Buscamos la mascota para que se puedan modificar sus datos
    mascota = Mascota.objects.get(id=id)
    razas = Raza.objects.all()
    estados = Estado.objects.all()
    generos = Genero.objects.all()

    variables = {
        'mascota':mascota,
        'razas':razas,
        'estados':estados,
        'generos': generos
    }

    if request.POST:
        mascota = Mascota()
        mascota.id = request.POST.get('txtId')
        mascota.nombreMascota = request.POST.get('txtNombreMascota')
        mascota.fechaIngreso = request.POST.get('dateFechaIngreso')
        mascota.fechaNacimientoMascota = request.POST.get('dateFechaNacimientoMascota')
        mascota.foto = request.FILES.get('fileFoto')
        estado = Estado() 
        estado.id = request.POST.get('cboEstado')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        genero = Genero()   
        genero.id = request.POST.get('cboGenero')
        mascota.raza = raza 
        mascota.estado = estado
        mascota.genero = genero

        try:
            mascota.save()
            messages.success(request, "La mascota " "'"+mascota.nombreMascota+"'" " se ha Modificado correctamente")
        except:
            messages.error(request, "La mascota " "'"+mascota.nombreMascota+"'" " no se ha podido modificar")
        return redirect('listado_mascotas') #Le estamos diciendo que si no se pudo modificar, que devuelva a la lista
    
    return render(request, 'core/modificar_mascota.html', variables)

def get_ciudades(request, id):
    ciudades=Ciudad.objects.filter(region=id)
    qs_json = serializers.serialize('json', ciudades)
    return HttpResponse(qs_json, content_type='application/json')

#def get_comunas(request, id):
    #comunas=Comuna.objects.filter(ciudad=id)
    #qs_json = serializers.serialize('json', comunas)
    #return HttpResponse(qs_json, content_type='application/json')