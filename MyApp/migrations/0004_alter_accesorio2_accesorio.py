# Generated by Django 4.1.5 on 2023-01-30 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_alter_accesorio2_imagenaccesorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio2',
            name='accesorio',
            field=models.CharField(choices=[('teclado', 'Teclados'), ('mouse', 'Mouses'), ('auricular', 'Auriculares')], max_length=15),
        ),
    ]
