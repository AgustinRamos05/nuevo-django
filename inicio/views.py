from django.shortcuts import render, redirect
from inicio.models import Iphone
from inicio.forms import ComprarIphoneForm, ActualizarIphoneForm


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

def eliminar(request, iphone_id):
   iphone_eliminado = Iphone.objects.get(id=iphone_id)
   iphone_eliminado.delete()
   return redirect('productos')

def actualizar(request, iphone_id):
   iphone_actualizar = Iphone.objects.get(id=iphone_id)
   
   if request.method == 'POST':
      formulario = ActualizarIphoneForm(request.POST)
      if formulario.is_valid():
         info_nueva = formulario.cleaned_data
         iphone_actualizar.modelo = info_nueva.get('modelo')
         iphone_actualizar.color = info_nueva.get('color')
         iphone_actualizar.memoria = info_nueva.get('memoria')
         
         iphone_actualizar.save()
         return redirect('productos')
      return render(request, 'inicio/actualizar_iphone.html', {'formulario': formulario})
         
   formulario = ActualizarIphoneForm(initial={'modelo': iphone_actualizar.modelo, 'color': iphone_actualizar.color, 'memoria': iphone_actualizar.memoria})
   return render(request, 'inicio/actualizar_iphone.html ',{'formulario': formulario})

def detalle_iphone(request, iphone_id):
   iphone = Iphone.objects.get(id=iphone_id)
   return render(request, 'inicio/detalle_iphone.html', {'iphone': iphone})