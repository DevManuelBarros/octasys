# Generated by Django 3.0.7 on 2020-06-07 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0013_auto_20200607_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='rango_precios',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='material_id_ran', to='generales.Materiales'),
        ),
    ]
