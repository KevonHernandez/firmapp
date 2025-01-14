from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=255)
    nick = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    salt = models.TextField()  # Salt en base64
    private_key = models.TextField()  # Clave privada cifrada en base64
    public_key = models.TextField()  # Clave pública en PEM
    iv = models.TextField()  # IV en base64
    salt_llave = models.TextField()  # Salt para la llave en base64
    
    def __str__(self):
        return self.nick
