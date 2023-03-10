# Generated by Django 4.1.5 on 2023-01-30 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accesorio', models.CharField(choices=[('teclado', 'Teclados'), ('mouse', 'Mouses'), ('auricular', 'Auriculares')], default='teclado', max_length=15)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagenAccesorio', models.ImageField(blank=True, null=True, upload_to='\\img')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='MyApp.accesorio2')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
        migrations.DeleteModel(
            name='Comprador',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
    ]
