# Generated by Django 3.0.7 on 2020-06-13 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0020_canales_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default='static/iamgen/no_img.jpg', upload_to='categoria'),
        ),
    ]
