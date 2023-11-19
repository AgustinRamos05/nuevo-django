from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import FormularioDeRegistro


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasena = formulario.cleaned_data.get('password') 
            
            user = authenticate(username=usuario, password=contrasena)
            django_login(request, user)
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