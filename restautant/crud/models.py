from django.db import models

# Create your models here.
class Formulario(models.Model):
    nombre=models.CharField(max_length=15)
    paterno=models.CharField(max_length=15)
    materno=models.CharField(max_length=15)
    rut=models.CharField(max_length=12)
    email=models.EmailField()
    comentarios=models.CharField(max_length=500)
    def __str__(self):
        return "rut: "+self.rut
    
class Principal(models.Model):
    nombre=models.CharField(max_length=15)
    categoria=models.CharField(max_length=15)
    precio=models.IntegerField()
    image = models.ImageField(verbose_name='Imagen',upload_to='media/principal',null=True,blank=True)    
    
    class Meta:
        verbose_name = 'principal'
        verbose_name_plural = 'principales'
        ordering = ['categoria','nombre']
    def __str__(self):
        return self.nombre
#principal, postre, bebestibles

class Postre(models.Model):
    nombre=models.CharField(max_length=15)
    categoria=models.CharField(max_length=15)
    precio=models.IntegerField()
    image = models.ImageField(verbose_name='Imagen',upload_to='media/postre',null=True,blank=True)    
    
    class Meta:
        ordering = ['categoria','nombre']
    def __str__(self):
        return self.nombre
    
class Bebestible(models.Model):
    nombre=models.CharField(max_length=15)
    categoria=models.CharField(max_length=15)
    precio=models.IntegerField()
    image = models.ImageField(verbose_name='Imagen',upload_to='media/bebestible',null=True,blank=True)    
    
    class Meta:
        ordering = ['categoria','nombre']
    def __str__(self):
        return self.nombre