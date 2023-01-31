from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()
    antiguedad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Marca: {self.marca} - Modelo: {self.modelo} - Precio: {self.precio}"

###########

class Accesorio2(models.Model):
    AccesorioSeleccion = (
    ('teclado','Teclados'),
    ('mouse', 'Mouses'),
    ('auricular','Auriculares'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    accesorio = models.CharField(max_length=30, choices=AccesorioSeleccion)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=140)
    year = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0) 
    imagen = models.ImageField(null=True, blank=True, upload_to="assets/")

    def __str__(self):
        return f"Accesorio: {self.accesorio} - Marca: {self.marca} - Modelo: {self.modelo} - Year: {self.year} - Precio:{self.precio}"

############

class Comentario(models.Model):
    comentario = models.ForeignKey(Accesorio2, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
