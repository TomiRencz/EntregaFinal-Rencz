from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from MyApp.models import Accesorio, Producto
from MyApp.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from MyApp.forms import CursoFormulario, ProfesorFormulario

def inicio(request):
        return render(request,"inicio.html")

def productos(request):
      if request.method == 'POST':
            miFormulario = ProductoFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Producto(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'],precio=informacion['precio'],antiguedad=informacion['antiguedad']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= AccesorioFormulario() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def accesorios(request):
      if request.method == 'POST':
            miFormulario = AccesorioFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'],precio=informacion['precio']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= AccesorioFormulario() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def teclados(request):
      if request.method == 'POST':
            miFormulario = AccesorioFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'],precio=informacion['precio']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= AccesorioFormulario() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def mouses(request):
      if request.method == 'POST':
            miFormulario = AccesorioFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'],precio=informacion['precio']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= AccesorioFormulario() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def auriculares(request):
      if request.method == 'POST':
            miFormulario = AccesorioFormulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'],precio=informacion['precio']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= AccesorioFormulario() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

# def compradores(request):
#       if request.method == 'POST':
#             miFormulario = AccesorioFormulario(request.POST) 
#             print(miFormulario)
#             if miFormulario.is_valid:   
#                   informacion = miFormulario.cleaned_data
#                   comprador = Comprador(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 
#                   comprador.save()
#                   return render(request, "inicio.html") 
#       else: 
#             miFormulario= AccesorioFormulario() 
#       return render(request, "compradores.html", {"miFormulario":miFormulario}) 

# def vendedores(request):
#       if request.method == 'POST':
#             miFormulario = VendedorFormulario(request.POST) 
#             print(miFormulario)
#             if miFormulario.is_valid:   
#                   informacion = miFormulario.cleaned_data
#                   vendedor = Vendedor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 
#                   vendedor.save()
#                   return render(request, "inicio.html") 
#       else: 
#             miFormulario= VendedorFormulario() 
#       return render(request, "vendedores.html", {"miFormulario":miFormulario})

# def empresas(request):
#       if request.method == 'POST':
#             miFormulario = EmpresasFormulario(request.POST) 
#             print(miFormulario)
#             if miFormulario.is_valid:   
#                   informacion = miFormulario.cleaned_data
#                   empresa = Empresa(nombre=informacion['nombre']) 
#                   empresa.save()
#                   return render(request, "inicio.html") 
#       else: 
#             miFormulario= EmpresasFormulario() 
#       return render(request, "empresas.html", {"miFormulario":miFormulario}) 

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre'] 
        productos = Accesorio.objects.filter(nombre__icontains=nombre)
        return render(request, "inicio.html", {"productos":productos, "nombre":nombre})
    else: 
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        contrasenia = request.POST['password']
        user = authenticate(request, username=usuario, password=contrasenia)
        if user is not None:
            login(request, user)
            return render(request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

#################

from django.contrib.auth.decorators import login_required

#################

@login_required
def inicio(request):

    return render(request, "inicio.html")

#################

def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:    
            form = UserRegisterForm()     
      return render(request,"registro.html" ,  {"form":form})

#################

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

#################

def logout_view(request):
    logout(request)
    # Redirect the user to the login page
    return redirect('login')

#################

def about(request):
    return render(request, 'acercaDeMi.html', {})

#################

def help(request):
    return render(request, 'ayuda.html', {})

#################

def contact(request):
    return render(request, 'contacto.html', {})

#################

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})

# #################

# # TECLADO

# class TecladoLista(LoginRequiredMixin, ListView):
#     context_object_name = 'teclados'
#     queryset = Accesorio.objects.filter(accesorio__startswith='teclado')
#     template_name = 'listaTeclados.html'

# class TecladoDetalle(LoginRequiredMixin, DetailView):
#     model = Accesorio
#     context_object_name = 'teclado'
#     template_name = 'tecladoDetalle.html'

# class TecladoUpdate(LoginRequiredMixin, UpdateView):
#     model = Accesorio
#     form_class = ActualizacionAccesorio
#     success_url = reverse_lazy('teclados')
#     context_object_name = 'teclado'
#     template_name = 'tecladoEdicion.html'

# class TecladoDelete(LoginRequiredMixin, DeleteView):
#     model = Accesorio
#     success_url = reverse_lazy('teclados')
#     context_object_name = 'teclado'
#     template_name = 'tecladoBorrado.html'

#################

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

class AccesorioCreacion(LoginRequiredMixin, CreateView):
    model = Accesorio
    form_class = FormularioNuevoAccesorio
    success_url = reverse_lazy('inicio')
    template_name = 'accesorioCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AccesorioCreacion, self).form_valid(form)