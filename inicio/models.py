from django.db import models

# Create your models here.

class Iphone(models.Model):
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    memoria = models.IntegerField()
    descripcion = models.TextField()
    
    def __str__(self):
        return f'{self.modelo} - color: {self.color}'