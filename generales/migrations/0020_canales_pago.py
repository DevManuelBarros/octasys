# Generated by Django 3.0.7 on 2020-06-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0019_auto_20200607_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='canales_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('porcentaje', models.FloatField()),
            ],
        ),
    ]
