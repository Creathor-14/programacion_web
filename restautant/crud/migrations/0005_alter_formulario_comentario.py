# Generated by Django 4.2.1 on 2023-06-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_plato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='comentario',
            field=models.CharField(max_length=500),
        ),
    ]
