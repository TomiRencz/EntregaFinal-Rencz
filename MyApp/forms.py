from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
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

class Accesorio2Formulario(forms.Form):
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

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }

# class FormularioNuevoAccesorio(forms.ModelForm):
#     class Meta:
#         model = Accesorio
#         fields = ('nombre','marca','modelo','precio')

#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
#             'marca' : forms.TextInput(attrs={'class': 'form-control'}),
#             'modelo' : forms.Select(attrs={'class': 'form-control'}),
#             'precio' : forms.TextInput(attrs={'class': 'form-control'}),
        # }

class FormularioNuevoAccesorio2(forms.ModelForm):
    class Meta:
        model = Accesorio2
        fields = ('usuario','accesorio','marca','modelo','descripcion','year','precio','imagen')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'accesorio' : forms.Select(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'modelo' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class': 'form-control'}),
            'year' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            }


class ActualizacionAccesorio(forms.ModelForm):
    class Meta:
        model = Accesorio2
        fields = ('marca','modelo','descripcion','year','precio','imagen')

class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')