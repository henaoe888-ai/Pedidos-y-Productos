from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    nombre = models.CharField(max_length=20)
    valor = models.DecimalField()
    estado = models.CharField()
    descripcion = models.TextField(max_length=100)
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)

def __str__(self):
    return self.nombre