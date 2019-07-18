from django import forms
from Apps.ModuloCompras.models import Producto,Provehedor
class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=[
            'nombre',
            'precio',

        ]
        labels={
            'nombre':'Nombre',
            'precio':'Precio',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),

        }
class ProvehedorForm(forms.ModelForm):
    class Meta:
        model=Provehedor
        fields=[
            'nombre',
            'apellido',
            'sexo',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellido',
            'sexo':'Sexo',
            'edad':'Edad',
            'telefono':'Telefono',
            'email':'Email',
            'domicilio':'Domicilio',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
        } 