# Generated by Django 3.0.7 on 2020-06-07 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0008_auto_20200607_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='caras',
            field=models.CharField(blank=True, choices=[('s', 'simple'), ('d', 'doble')], default='s', max_length=5),
        ),
    ]
