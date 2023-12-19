from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioDeRegistro(UserCreationForm):
    username = forms.CharField(label='Usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        help_text = {key: '' for key in fields}
        
class FormularioDeEdicion(UserChangeForm):
    
    password = None
    email = forms.EmailField(label='Cambiar Email', required=False)
    first_name = forms.CharField(label='Cambiar Nombre', required=False)
    last_name = forms.CharField(label='Cambiar Apellido', required=False)
    descripcion = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = [ 'email','first_name', 'last_name', 'descripcion', 'avatar']
        