# Generated by Django 4.1.5 on 2023-01-31 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_accesorio2_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio2',
            name='accesorio',
            field=models.CharField(choices=[('teclado', 'Teclados'), ('mouse', 'Mouses'), ('auricular', 'Auriculares')], max_length=30),
        ),
        migrations.AlterField(
            model_name='accesorio2',
            name='descripcion',
            field=models.CharField(max_length=140),
        ),
    ]