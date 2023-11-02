from django.shortcuts import render, redirect
from inicio.models import Iphone
from inicio.forms import ComprarIphoneForm


def inicio(request):
   return render(request, 'inicio/inicio.html', {})
   
def iphones(request):
   
   modelo_buscado = request.GET.get('modelo')
   
   if modelo_buscado:
      listado_iphones = Iphone.objects.filter(modelo__icontains=modelo_buscado)
   else:
      listado_iphones = Iphone.objects.all()
   

   return render(request, 'inicio/iphones.html', {'listado_iphones': listado_iphones})

def comprar_iphone(request):
   
   if request.method == 'POST':
      formulario = ComprarIphoneForm(request.POST)
      if formulario.is_valid():
         
         modelo = request.POST.get('modelo')
         color = request.POST.get('color')
         memoria = request.POST.get('memoria')
         
         iphone = Iphone(modelo=modelo,color=color,memoria=memoria)
         iphone.save()
         
         return redirect('productos')
      else:
         return render(request, 'inicio/comprar_iphone.html',{'formulario': formulario}) 
         
         
   formulario = ComprarIphoneForm() 
   return render(request, 'inicio/comprar_iphone.html',{'formulario': formulario})  