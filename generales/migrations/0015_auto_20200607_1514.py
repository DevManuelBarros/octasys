# Generated by Django 3.0.7 on 2020-06-07 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0014_rango_precios_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rango_precios',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_id_ran', to='generales.Materiales'),
        ),
    ]