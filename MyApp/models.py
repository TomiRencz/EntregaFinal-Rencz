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

# class Accesorio(models.Model):
#     AccesorioSeleccion = (
#     ('teclado','Teclados'),
#     ('mouse', 'Mouses'),
#     ('auricular','Auriculares'),
#     )
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     accesorio = models.CharField(max_length=15, choices=AccesorioSeleccion, default='guitarra')
#     marca = models.CharField(max_length=40)
#     modelo = models.CharField(max_length=40)
#     descripcion = models.TextField(null=True, blank=True)
#     year = models.IntegerField() 
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     fechaPublicacion = models.DateTimeField(auto_now_add=True)
#     telefonoContacto = models.IntegerField()
#     emailContacto = models.EmailField()
#     imagenAccesorio = models.ImageField(null=True, blank=True, upload_to="\img")

    # class Meta:
    #     ordering = ['usuario', '-fechaPublicacion']

    # def __str__(self):
    #     return self.titulo

class Accesorio(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Marca: {self.marca} - Modelo: {self.modelo} - Precio: {self.precio} "
###########

# class Vendedor(models.Model):
#     nombre= models.CharField(max_length=30)
#     apellido= models.CharField(max_length=30)
#     email= models.EmailField()

#     def __str__(self):
#         return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email}"

###########

# class Comprador(models.Model):
#     nombre= models.CharField(max_length=30)
#     apellido= models.CharField(max_length=30)
#     email= models.EmailField()

#     def __str__(self):
#         return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email}"

###########

# class Empresa(models.Model):
#     nombre = models.CharField(max_length=30)

#     def __str__(self):
#         return f"Nombre: {self.nombre}"

###########

class Comentario(models.Model):
    comentario = models.ForeignKey(Accesorio, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)