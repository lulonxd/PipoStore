# Generated by Django 3.1.2 on 2020-11-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProductos', '0005_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(max_length=7),
        ),
    ]
