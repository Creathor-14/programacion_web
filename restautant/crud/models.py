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
    
class Plato(models.Model):
    nombre=models.CharField(max_length=15)
    categoria=models.CharField(max_length=15)
    precio=models.IntegerField()
    #imagen=models.ImageField(upload_to='productos')
    def __str__(self):
        return self.nombre
#principal, postre, bebestibles