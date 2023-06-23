# Generated by Django 4.2.1 on 2023-06-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('ap_paterno', models.CharField(max_length=15)),
                ('ap_materno', models.CharField(max_length=15)),
                ('rut', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=9)),
                ('comentario', models.CharField(max_length=300)),
            ],
        ),
    ]
