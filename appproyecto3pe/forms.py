from django import forms

class AsesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    id_asesor = forms.CharField(max_length=30)