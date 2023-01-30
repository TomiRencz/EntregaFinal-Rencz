from django.urls import path
from MyApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('teclados', views.teclados, name="Teclados"),
    path('auriculares', views.auriculares, name="Auriculares"),
    path('mouses', views.mouses, name="Mouses"),
    path('productos', views.productos, name="Productos"),
    path('register', views.register, name='Register'),
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('passwordCambio/', views.CambioPassword.as_view(), name="cambiar_password"),
    path('passwordExitoso/', views.password_exitoso, name="password_exitoso"),
    path('editarPerfil/', views.editarPerfil, name="Editar_Perfil"),
    path('acercaDeMi/', views.about, name="acerca_de_mi"),
    path('ayuda/', views.help, name="Ayuda"),
    path('contacto/', views.contact, name="Contacto"),
    path('buscar/', views.buscar),
    # path('listaTeclados/', views.TecladoLista.as_view(), name="Teclados"),
    # path('tecladoDetalle/<int:pk>/', views.TecladoDetalle.as_view(), name='teclado'),
    # path('tecladoEdicion/<int:pk>/', views.TecladoUpdate.as_view(), name='teclado_editar'),
    # path('tecladoBorrado/<int:pk>/', views.TecladoDelete.as_view(), name='teclado_eliminar'),
    # path('tecladoDetalle/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),
]