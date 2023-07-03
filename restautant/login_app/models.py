from django.db import models
import re
# Create your models here.


# Create your models here.
class UserManager(models.Manager):
    def validador_campos(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        JUST_LETTERS = re.compile(r'^[a-zA-Z.]+$')
        PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$')

        errores = {}

        if len(Usuario.objects.filter(email=postData['email'])) > 0:
            errores['email_exits'] = "Email ya registrado!!!"
        else:
            if len(postData['nombre'].strip()) < 2 or len(postData['nombre'].strip()) > 30:
                errores['nombre_len'] = "Nombre debe tener entre 2 y 30 caracteres"

            if len(postData['apellido'].strip()) < 2 or len(postData['apellido'].strip()) > 30:
                errores['apellido_len'] = "Apellido debe tener entre 2 y 30 caracteres"
            
            if not JUST_LETTERS.match(postData['nombre']) or not JUST_LETTERS.match(postData['apellido']):
                errores['just_letters'] = "Solo se permite el ingreso de letras en el nombre y apellido"
                
            if not EMAIL_REGEX.match(postData['email']):
                errores['email'] = "Formato correo no válido"
            
            if not PASSWORD_REGEX.match(postData['clave']):
                errores['clave_format'] = "Formato contraseña no válido"

        #if len(postData['clave']) < 8 or len(postData['clave']) > 15:
        #    errores['clave_len'] = "La cantidad de caracteres debe ser entre 8 y 15" 

        #if postData['clave'] != postData['clave_confirm']:
        #    errores['clave_confirm'] = "Contraseñas no coinciden"

        return errores

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    clave = models.CharField(max_length=250)
    rol = models.CharField(max_length=20, default='USER')

    objects = UserManager()

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ["email"]

    def __repr__(self) -> str:
        return self.nombre + " " + self.apellido