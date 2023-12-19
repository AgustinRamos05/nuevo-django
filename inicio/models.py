from django.db import models
from ckeditor.fields import RichTextField

class Iphone(models.Model):
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    memoria = models.IntegerField()
    descripcion = RichTextField()
    
    def __str__(self):
        return f'{self.modelo} - color: {self.color}'