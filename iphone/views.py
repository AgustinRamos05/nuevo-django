from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from iphone.models import Mac
from django.urls import reverse_lazy

class ListadoProductos(ListView):
    model = Mac
    context_object_name = 'listado_productos'
    template_name = 'iphone/iphone.html'   
    
class CrearIphone(CreateView):
    model = Mac
    template_name = "iphone/crear_iphone.html"
    fields = ['modelo','color','descripcion','memoria']
    success_url = reverse_lazy('iphone')
    
class ActualizarIphone(UpdateView):
    model = Mac
    template_name = "iphone/actualizar_iphone.html"
    fields = ['modelo','color','descripcion','memoria']
    success_url = reverse_lazy('iphone')

class DetalleIphone(DetailView):
    model = Mac
    template_name = "iphone/detalle_producto.html"
    
class EliminarIphone(DeleteView):
    model = Mac
    template_name = "iphone/eliminar_producto.html"
    success_url = reverse_lazy('iphone')
