from django.db import models 


# Create your models here.

class Cliente(models.Model):
    codigo = models.CharField(max_length=200,unique=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'clientes'
        verbose_name_plural = 'clientes'
    

    def __str__(self):
        return self.nombre

class Autos(models.Model):
    placa = models.CharField(max_length=200,unique=True)
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    horaEntrada = models.DateTimeField()
    horaSalida = models.DateTimeField()
    
    
    class Meta:
        verbose_name = 'autos'
        verbose_name_plural = 'autos'
        

    def __str__(self):
        return self.placa

