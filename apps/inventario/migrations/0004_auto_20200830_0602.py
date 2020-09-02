# Generated by Django 3.1 on 2020-08-30 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_insumos_unidadmedida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumos',
            name='unidad_medida',
            field=models.ForeignKey(default='sin categoria', on_delete=django.db.models.deletion.CASCADE, to='inventario.unidadmedida'),
        ),
    ]