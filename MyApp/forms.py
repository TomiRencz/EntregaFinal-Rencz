from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from MyApp.models import *

# class VendedorFormulario(forms.Form):
#     nombre= forms.CharField(max_length=30)
#     apellido= forms.CharField(max_length=30)
#     email= forms.EmailField()  

# class CompradorFormulario(forms.Form):
#     nombre= forms.CharField(max_length=30)
#     apellido= forms.CharField(max_length=30)
#     email= forms.EmailField()  

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    antiguedad = forms.IntegerField()

class AccesorioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    precio = forms.IntegerField()

# class EmpresasFormulario(forms.Form):
#     nombre = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ActualizacionAccesorio(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ('nombre','marca','modelo','precio')


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormularioNuevoAccesorio(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ('nombre','marca','modelo','precio')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.Select(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
        }