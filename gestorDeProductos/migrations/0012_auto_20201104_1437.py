# Generated by Django 3.1.2 on 2020-11-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProductos', '0011_auto_20201103_1915'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
