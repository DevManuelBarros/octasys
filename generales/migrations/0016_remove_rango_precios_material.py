# Generated by Django 3.0.7 on 2020-06-07 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0015_auto_20200607_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rango_precios',
            name='material',
        ),
    ]