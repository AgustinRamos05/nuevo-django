from django import forms

class BaseIphoneForm(forms.Form):
    modelo = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    memoria = forms.IntegerField()
    
    
class ComprarIphoneForm(BaseIphoneForm):
    ...
    
class ActualizarIphoneForm(BaseIphoneForm):
    ...