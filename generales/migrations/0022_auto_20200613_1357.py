# Generated by Django 3.0.7 on 2020-06-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0021_categoria_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen_principal',
            field=models.ImageField(default='no_img.jpg', upload_to='producto'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default='no_img.jpg', upload_to='categoria'),
        ),
    ]