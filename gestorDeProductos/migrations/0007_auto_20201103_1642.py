# Generated by Django 3.1.2 on 2020-11-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProductos', '0006_auto_20201103_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
