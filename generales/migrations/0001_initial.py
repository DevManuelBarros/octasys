# Generated by Django 3.0.7 on 2020-06-06 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=255)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unidad_de_medida', models.CharField(choices=[('g', 'gramo/s'), ('k', 'kilo/s'), ('cm2', 'centimetro/ cuadrado/s'), ('cm', 'centimetro/s'), ('m', 'metros')], default='g', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('forma', models.CharField(choices=[('circ', 'Circular'), ('rect', 'Rectangular'), ('cuad', 'Cuadrado'), ('irre', 'Irregular'), ('tria', 'Triangular'), ('oval', 'Ovalada')], max_length=5)),
                ('medida1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('medida2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('medida3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descripcion', models.CharField(max_length=255)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_id', to='generales.Categoria')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materiales_id', to='generales.Materiales')),
            ],
        ),
    ]
