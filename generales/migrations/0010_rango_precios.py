# Generated by Django 3.0.7 on 2020-06-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0009_auto_20200607_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='rango_precios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_presta', models.IntegerField()),
                ('categoria_ml', models.IntegerField()),
                ('cantidad_pack', models.IntegerField()),
                ('cantidad_minima', models.IntegerField()),
                ('cantidad_maxima', models.IntegerField()),
                ('porcetaje', models.FloatField()),
            ],
        ),
    ]
