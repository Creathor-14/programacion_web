from django.db import models

# Create your models here.

class Formulario(models.Model):
    nombre=models.CharField(max_length=15)
    ap_paterno=models.CharField(max_length=15)
    ap_materno=models.CharField(max_length=15)
    rut=models.CharField(max_length=12)
    email=models.EmailField()
    #telefono=models.CharField(max_length=9)
    comentario=models.CharField(max_length=300)

class Producto(models.Model):
    nombre=models.CharField(max_length=15)
    categoria=models.CharField(max_length=15)
    precio=models.IntegerField()
    imagen=models.ImageField(upload_to='productos')
    
    
class Nosotros(models.Model):
    nombre=models.CharField(max_length=15)
    ap_paterno=models.CharField(max_length=15)
    ap_materno=models.CharField(max_length=15)
    email=models.EmailField()
    descripcion=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='nosotros')

from django.db import models

# Create your models here.
class Platform(models.Model):
    platform = models.CharField(verbose_name='Plataforma', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'plataforma'
        verbose_name_plural = 'plataformas'
        ordering = ['platform']

    def __str__(self) -> str:
        return self.platform

class VideoGame(models.Model):
    idVideogame = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    title = models.CharField(verbose_name='Título',max_length=250)
    platform = models.ForeignKey(Platform,verbose_name='Plataforma',on_delete=models.CASCADE)
    studio = models.CharField(verbose_name='Estudio',max_length=50)
    value = models.IntegerField(verbose_name='Valor unitario')
    stock = models.IntegerField(verbose_name='Stock')
    image = models.ImageField(verbose_name='Imagen',upload_to='videojuegos',null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'videojuego'
        verbose_name_plural = 'videojuegos'
        ordering = ['title','platform']

    def __str__(self) -> str:
        return self.title