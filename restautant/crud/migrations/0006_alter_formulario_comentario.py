# Generated by Django 4.2.2 on 2023-06-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_remove_formulario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='comentario',
            field=models.CharField(max_length=500),
        ),
    ]
