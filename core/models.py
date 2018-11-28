from django.db import models

# Create your models here.

class Region(models.Model):
    #Django agrega un Id a todos los modelos(autoincrementable)
    nombreRegion = models.CharField(max_length=50)

    # Con el siguiente metodo o funcion estamos haciendo que en vez de Objects() nos salga el nombre
    # de la region
    def __str__(self):
        return self.nombreRegion 

    #Esta subclase permite otorgarle a los plurales a los sustantivos, ya que Django no sabe hablar
    #español solo le agrega una S a todo
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
        

class Ciudad(models.Model):
    nombreCiudad = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCiudad

    def as_dict(self):
        return {
            "id": self.id,
            "nombreCiudad":self.nombreCiudad,
        }
    class Meta:
        verbose_name="Ciudad"
        verbose_name_plural = "Ciudades"  

#class Comuna(models.Model):
#    nombre_comuna= models.CharField(max_length=250)
#    ciudad  = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

#    def _str_(self):
#        return self.nombre_comuna
#    def as_dict(self):
#        return {
#            "id": self.id,
#            "nombre_comuna":self.nombre_comuna,
#        }
#    class Meta:
#        verbose_name="Comuna"
#        verbose_name_plural = "Comunas"  

class TipoVivienda(models.Model):
    nombreVivienda = models.CharField(max_length=60)

    def __str__(self):
        return self.nombreVivienda

class Postulante(models.Model):
    correo = models.CharField(max_length=60)
    rut = models.CharField(max_length=12, unique=True)
    nombreCompleto = models.CharField(max_length=60)
    fechaNacimiento = models.DateField()
    telefono  = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    tipoVivienda = models.ForeignKey(TipoVivienda, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreCompleto
        

class Raza(models.Model):
    nombreRaza = models.CharField(max_length=60)

    def __str__(self):
        return self.nombreRaza

class Estado(models.Model):
    nombreEstado = models.CharField(max_length=60)

    def __str__(self):
        return self.nombreEstado

class Genero(models.Model):
    nombreGenero = models.CharField(max_length=1)

    def __str__(self):
        return self.nombreGenero

    def genero_formato(self):

        if self.nombreGenero == "M":
            genero = "Macho"
        else:
            genero = "Hembra"

        return genero

class Mascota(models.Model):
    nombreMascota = models.CharField(max_length=60)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fechaIngreso = models.DateField()
    fechaNacimientoMascota = models.DateField(null=True, blank=True)
    foto = models.FileField(upload_to="media/", null=False )
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMascota

    def fecha_ingreso_formato(self):
        return self.fechaIngreso.strftime("%Y-%m-%d")

    def fecha_nacimiento_formato(self):
        return self.fechaNacimientoMascota.strftime("%Y-%m-%d")

    def genero_formato(self):

        if self.genero_id == 1:
            genero = "Macho"
        else:
            genero = "Hembra"

        return genero

    class Meta:

        permissions = (

            ('puede_agregar', 'agrega mascotas'),
        )

    
    





