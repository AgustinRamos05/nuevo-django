from django.db import models

# Create your models here.
class Mac(models.Model):
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    memoria = models.IntegerField()
    
    def __str__(self) :
        return f'{self.modelo} Color: {self.color}'