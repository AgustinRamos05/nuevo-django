from django.shortcuts import render
from inicio.models import Iphone

def inicio(request):
   return render(request, 'inicio/inicio.html', {})
   
def iphones(request):
   
   iphone = Iphone(modelo='Iphone 12',color='rojo',memoria=64 ,descripcion='usado')
   iphone.save()
   return render(request, 'inicio/iphones.html', {'iphone': iphone})