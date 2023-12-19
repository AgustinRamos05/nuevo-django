from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from cuentas.forms import FormularioDeRegistro, FormularioDeEdicion
from cuentas.models import DatosExtra


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasena = formulario.cleaned_data.get('password') 
            
            user = authenticate(username=usuario, password=contrasena)
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('inicio')
        else:
            return render(request, 'cuentas/login.html', {'form_login': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'form_login': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioDeRegistro(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    formulario = FormularioDeRegistro()
    return render(request, 'cuentas/registro.html', {'form_registro': formulario})

def mostrar_perfil(request):
    
    datos_usuario = request.user
    
    return render(request, 'cuentas/datos_usuario.html',{'datos_usuario': datos_usuario})

def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = FormularioDeEdicion(initial={'descripcion':datos_extra.descripcion, 'avatar': datos_extra.avatar}, instance=request.user)
    
    if request.method == 'POST':
        formulario = FormularioDeEdicion(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            nueva_descripcion = formulario.cleaned_data.get('descripcion')
            nuevo_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_descripcion:
                datos_extra.descripcion = nueva_descripcion
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar
                # request.user.datosextra.descripcion = nueva_descripcion
                # request.user.datosextra.save()
            datos_extra.save()   
            formulario.save()
            return redirect('mostrar_perfil')
    
    return render(request, 'cuentas/editar_perfil.html', {'formulario_edicion': formulario})

class CambiarPassword(PasswordChangeView):
    
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('mostrar_perfil')