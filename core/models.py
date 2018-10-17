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

    def __str__(self):
        return self.nombreCiudad

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

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
        return self.correo
        return self.rut
        return self.nombreCompleto
        return self.fechaNacimiento
        return self.telefono
        return self.region
        return self.tipoVivienda
        return self.ciudad

class Raza(models.Model):
    nombreRaza = models.CharField(max_length=60)

    def __str__(self):
        return self.nombreRaza

class Estado(models.Model):
    nombreEstado = models.CharField(max_length=60)

    def __str__(self):
        return self.nombreEstado

class Mascota(models.Model):
    nombreMascota = models.CharField(max_length=60)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = models.CharField(max_length=1)
    fechaIngreso = models.DateField()
    fechaNacimientoMascota = models.DateField(null=True)
    foto = models.ImageField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    





