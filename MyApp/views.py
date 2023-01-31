from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from MyApp.models import Accesorio2
from MyApp.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from MyApp.forms import CursoFormulario, ProfesorFormulario

def inicio(request):
        return render(request,"inicio.html")

# def productos(request):
#       if request.method == 'POST':
#             miFormulario = ProductoFormulario(request.POST) 
#             print(miFormulario)
#             if miFormulario.is_valid:   
#                   informacion = miFormulario.cleaned_data
#                   producto = Producto(nombre=informacion['nombre'], marca=informacion['marca'], modelo=informacion['modelo'],precio=informacion['precio'],antiguedad=informacion['antiguedad']) 
#                   producto.save()
#                   return render(request, "inicio.html") 
#       else: 
#             miFormulario= ProductoFormulario() 
#       return render(request, "productos.html", {"miFormulario":miFormulario}) 

def accesorios(request):
      if request.method == 'POST':
            miFormulario = Accesorio2Formulario(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio2(usuario=informacion['usuario'], nombre=informacion['accesorio'], marca=informacion['marca'],modelo=informacion['modelo'],descripcion=informacion['descripcion'],precio=informacion['precio'],imagen=informacion['imagen']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= Accesorio2Formulario() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def teclados(request):
      if request.method == 'POST':
            miFormulario = FormularioNuevoAccesorio2(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio2(usuario=informacion['usuario'], nombre=informacion['accesorio'], marca=informacion['marca'],modelo=informacion['modelo'],descripcion=informacion['descripcion'],precio=informacion['precio'],imagen=informacion['imagen']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= FormularioNuevoAccesorio2() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def mouses(request):
      if request.method == 'POST':
            miFormulario = FormularioNuevoAccesorio2(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio2(usuario=informacion['usuario'], nombre=informacion['accesorio'], marca=informacion['marca'],modelo=informacion['modelo'],descripcion=informacion['descripcion'],precio=informacion['precio'],imagen=informacion['imagen']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= FormularioNuevoAccesorio2() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def auriculares(request):
      if request.method == 'POST':
            miFormulario = FormularioNuevoAccesorio2(request.POST) 
            print(miFormulario)
            if miFormulario.is_valid:   
                  informacion = miFormulario.cleaned_data
                  producto = Accesorio2(usuario=informacion['usuario'], nombre=informacion['accesorio'], marca=informacion['marca'],modelo=informacion['modelo'],descripcion=informacion['descripcion'],precio=informacion['precio'],imagen=informacion['imagen']) 
                  producto.save()
                  return render(request, "inicio.html") 
      else: 
            miFormulario= FormularioNuevoAccesorio2() 
      return render(request, "productos.html", {"miFormulario":miFormulario}) 

def buscar(request):
    if request.GET["marca"]:
        marca = request.GET['marca'] 
        accesorio = Accesorio2.objects.filter(marca__icontains=marca)
        return render(request, "inicio.html", {"accesorio":accesorio, "marca":marca})
    else:
        respuesta= "No se ingresaron datos"
    return render(request, "inicio.html", {'respuesta':respuesta})

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

def contact_response(request):
    return render(request, 'contactoRespuesta.html', {})

#################

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})

# #################

# # TECLADO

class TecladoLista(LoginRequiredMixin, ListView):
    context_object_name = 'teclado'
    queryset = Accesorio2.objects.filter(accesorio__startswith='teclado')
    template_name = 'listaTeclados.html'

class TecladoDetalle(LoginRequiredMixin, DetailView):
    model = Accesorio2
    context_object_name = 'teclado'
    template_name = 'tecladoDetalle.html'

class TecladoUpdate(LoginRequiredMixin, UpdateView):
    model = Accesorio2
    form_class = ActualizacionAccesorio
    success_url = reverse_lazy('Teclados')
    context_object_name = 'teclado'
    template_name = 'tecladoEdicion.html'

class TecladoDelete(LoginRequiredMixin, DeleteView):
    model = Accesorio2
    success_url = reverse_lazy('Teclados')
    context_object_name = 'teclado'
    template_name = 'tecladoBorrado.html'

# # AURICULAR

class AuricularLista(LoginRequiredMixin, ListView):
    context_object_name = 'auricular'
    queryset = Accesorio2.objects.filter(accesorio__startswith='auricular')
    template_name = 'listaAuriculares.html'

class AuricularDetalle(LoginRequiredMixin, DetailView):
    model = Accesorio2
    context_object_name = 'auricular'
    template_name = 'auricularDetalle.html'

class AuricularUpdate(LoginRequiredMixin, UpdateView):
    model = Accesorio2
    form_class = ActualizacionAccesorio
    success_url = reverse_lazy('Auriculares')
    context_object_name = 'auricular'
    template_name = 'auricularEdicion.html'

class AuricularDelete(LoginRequiredMixin, DeleteView):
    model = Accesorio2
    success_url = reverse_lazy('Auriculares')
    context_object_name = 'auricular'
    template_name = 'auricularBorrado.html'

# # MOUSE

class MouseLista(LoginRequiredMixin, ListView):
    context_object_name = 'mouse'
    queryset = Accesorio2.objects.filter(accesorio__startswith='mouse')
    template_name = 'listaMouses.html'

class MouseDetalle(LoginRequiredMixin, DetailView):
    model = Accesorio2
    context_object_name = 'mouse'
    template_name = 'mouseDetalle.html'

class MouseUpdate(LoginRequiredMixin, UpdateView):
    model = Accesorio2
    form_class = ActualizacionAccesorio
    success_url = reverse_lazy('Mouses')
    context_object_name = 'mouse'
    template_name = 'mouseEdicion.html'

class MouseDelete(LoginRequiredMixin, DeleteView):
    model = Accesorio2
    success_url = reverse_lazy('Mouses')
    context_object_name = 'mouse'
    template_name = 'mouseBorrado.html'

#################

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

class AccesorioCreacion2(LoginRequiredMixin, CreateView):
    model = Accesorio2
    form_class = FormularioNuevoAccesorio2
    success_url = reverse_lazy('inicio')
    template_name = 'accesorioCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AccesorioCreacion2, self).form_valid(form)

#################

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user