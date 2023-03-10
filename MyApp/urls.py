from django.urls import path
from MyApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="inicio"),
    # path('teclados', views.teclados, name="Teclados"),
    # path('auriculares', views.auriculares, name="Auriculares"),
    # path('mouses', views.mouses, name="Mouses"),
    # path('accesorios', views.accesorios, name="Accesorios"),

    path('register', views.register, name='Register'),
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('passwordCambio/', views.CambioPassword.as_view(), name="cambiar_password"),
    path('passwordExitoso/', views.password_exitoso, name="password_exitoso"),
    path('edicionPerfil/', views.UsuarioEdicion.as_view(), name="editar_perfil"),

    path('acercaDeMi/', views.about, name="acerca_de_mi"),

    path('ayuda/', views.help, name="Ayuda"),
    path('contacto/', views.contact, name="Contacto"),
    path('contactoRespuesta/', views.contact_response, name="ContactoRespuesta"),

    path('buscar/', views.buscar),

    path('listaTeclados/', views.TecladoLista.as_view(), name="Teclados"),
    path('tecladoDetalle/<int:pk>/', views.TecladoDetalle.as_view(), name='teclado'),
    path('tecladoEdicion/<int:pk>/', views.TecladoUpdate.as_view(), name='teclado_editar'),
    path('tecladoBorrado/<int:pk>/', views.TecladoDelete.as_view(), name='teclado_eliminar'),
    path('tecladoDetalle/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),

    path('listaAuriculares/', views.AuricularLista.as_view(), name="Auriculares"),
    path('auricularDetalle/<int:pk>/', views.AuricularDetalle.as_view(), name='auricular'),
    path('auricularEdicion/<int:pk>/', views.AuricularUpdate.as_view(), name='auricular_editar'),
    path('auricularBorrado/<int:pk>/', views.AuricularDelete.as_view(), name='auricular_eliminar'),
    path('auricularDetalle/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),

    path('listaMouses/', views.MouseLista.as_view(), name="Mouses"),
    path('mouseDetalle/<int:pk>/', views.MouseDetalle.as_view(), name='mouse'),
    path('mouseEdicion/<int:pk>/', views.MouseUpdate.as_view(), name='mouse_editar'),
    path('mouseBorrado/<int:pk>/', views.MouseDelete.as_view(), name='mouse_eliminar'),
    path('mouseDetalle/<int:pk>/comentario/', views.ComentarioPagina.as_view(), name='comentario'),

    path('accesorioCreacion/', views.AccesorioCreacion2.as_view(), name='Nuevo'),
]