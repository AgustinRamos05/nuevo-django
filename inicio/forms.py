from django import forms
from ckeditor.fields import RichTextFormField

class BaseIphoneForm(forms.Form):
    modelo = RichTextFormField()
    color = forms.CharField(max_length=30)
    memoria = forms.IntegerField()
    
    
class ComprarIphoneForm(BaseIphoneForm):
    ...
    
class ActualizarIphoneForm(BaseIphoneForm):
    ...