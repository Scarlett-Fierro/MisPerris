from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

#El serializer permite transformar un arreglo en un json
from django.core import serializers
import json
from core.models import Mascota, Raza, Genero, Estado

from django.views.decorators.http import require_http_methods

#Este nos va servir para controlar un error 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from fcm_django.models import FCMDevice

@csrf_exempt
@require_http_methods(['POST'])
def agregar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    #Obtenemos el token
    token = bodyDict['token']

    #Primero verificamos que el token no exista en la BDD para guardarlo
    existe = FCMDevice.objects.filter(registration_id=token, active=True)

    if existe:
        return HttpResponseBadRequest(json.dumps({'mensaje': 'El token ya existe'}), content_type="aplication/json")

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    #Solo en caso de que el usuario este autenticado lo vamos a guardar o asociar con el token
    if request.user.is_authenticated:
        dispositivo.user = request.user

    #Procedemos a guardar el dispositivo con el token en la base de datos
    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje': 'Token Guardado correctamente'}), content_type="aplication/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje': 'No se ha podido guardar el Token'}), content_type="aplication/json")


#Crearemos un view que muestre el listado de mascotas en formato json

def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    #Tranformar los datos a Json
    mascotasJson = serializers.serialize('json', mascotas) 

    #Mostramos el json en el navegador
    return HttpResponse(mascotasJson, content_type="application/json")

#POST
@csrf_exempt
@require_http_methods(['POST']) #Esto va a indicar que solo va a recibir datos que entran de POST
def agregar_mascota(request):
    #Obtenemos el body del request
    body = request.body.decode('utf-8')
    #El body viene como un String, por lo que hay que transformarlo
    bodyDict = json.loads(body)

    #Guardaremos la mascota en la base de datos
    mascota = Mascota()
    mascota.nombreMascota = bodyDict['nombreMascota']
    mascota.fechaIngreso = bodyDict['fechaIngreso']
    mascota.fechaNacimientoMascota = bodyDict['fechaNacimientoMascota']
    # mascota.foto = bodyDict['foto']
    mascota.raza = Raza (id=bodyDict['raza']) #asi se hace
    mascota.genero = Genero (id=bodyDict['genero'])
    mascota.estado = Estado (id=bodyDict['estado'])
    
    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje': 'Guardado correctamente'}), content_type="aplication/json" )
    except:
        #Retornaremos un mensaje con codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje': 'No se ha podido guardar'}), content_type="aplication/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request,id):

    try:
        #primero buscamos la mascota que eliminaremos
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        return HttpResponse(json.dumps({'mensaje': 'Eliminado correctamente'}), content_type="application/json")
        #Con el content_type se le esta indicando que viene en formato Json
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje': 'No se ha podido eliminar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
     #Obtenemos el body del request
    body = request.body.decode('utf-8')
    #El body viene como un String, por lo que hay que transformarlo
    bodyDict = json.loads(body)

    #Guardaremos la mascota en la base de datos
    mascota = Mascota()
    mascota.id = bodyDict['id']
    mascota.nombreMascota = bodyDict['nombreMascota']
    mascota.fechaIngreso = bodyDict['fechaIngreso']
    mascota.fechaNacimientoMascota = bodyDict['fechaNacimientoMascota']
    # mascota.foto = bodyDict['foto']
    mascota.raza = Raza(id=bodyDict['raza']) #asi se hace
    mascota.genero = Genero(id=bodyDict['genero'])
    mascota.estado = Estado(id=bodyDict['estado'])
    
    
    try:
        mascota.save()
        return HttpResponse(json.dumps({'mensaje': 'Modificado correctamente'}), content_type="aplication/json" )
    except:
        #Retornaremos un mensaje con codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje': 'No se ha podido modificar'}), content_type="aplication/json")