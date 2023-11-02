from django import forms

class ComprarIphoneForm(forms.Form):
    modelo = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    memoria = forms.IntegerField()
    