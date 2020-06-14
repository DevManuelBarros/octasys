from django.db import models

#============ VARIABLES ================
from .utils import *

class Materiales(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    descripcion = models.CharField(max_length=255)
    costo = models.FloatField()
    unidad_de_medida = models.CharField(max_length=5, choices=unidades, default='g')
    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    descripcion = models.TextField()
    peso = models.BooleanField(default=True)
    forma = models.BooleanField(default=True)
    medida1 = models.BooleanField(default=False)
    medida2 = models.BooleanField(default=False)
    medida1_int = models.BooleanField(default=False)
    medida2_int = models.BooleanField(default=False)
    medida1_ext = models.BooleanField(default=False)
    medida2_ext = models.BooleanField(default=False)
    caras = models.BooleanField(default=False)
    color = models.BooleanField(default=False)
    categoria_presta = models.IntegerField(default=16)
    categoria_ml =models.IntegerField(default=0)
    imagen = models.ImageField(upload_to = 'categoria', default='no_img.jpg')
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, unique=True)
    peso = models.DecimalField(max_digits=numberDigits, decimal_places=decimalPlaces)
    material = models.ForeignKey(Materiales, related_name="materiales_id", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name="categoria_id", on_delete=models.CASCADE)
    forma = models.CharField(max_length=5, choices=formas)
    medida1 = models.DecimalField(max_digits=numberDigits, decimal_places=decimalPlaces, default=0, blank=True)
    medida2 = models.DecimalField(max_digits=numberDigits, decimal_places=decimalPlaces, default=0, blank=True)
    medida1_int = models.DecimalField(max_digits=numberDigits, decimal_places=decimalPlaces, default=0, blank=True)
    medida2_int = models.DecimalField(max_digits=numberDigits, decimal_places=decimalPlaces, default=0, blank=True)
    medida1_ext = models.DecimalField(max_digits=numberDigits, decimal_places=decimalPlaces, default=0, blank=True)
    medida2_ext = models.DecimalField(max_digits=numberDigits, decimal_places=decimalPlaces, default=0, blank=True)
    descripcion = models.TextField()
    color = models.CharField(max_length=400, blank=True)
    caras = models.CharField(max_length=5, choices=(('s','simple'),('d','doble')), blank=True, default='s')
    imagen_principal = models.ImageField(upload_to = 'producto', default='no_img.jpg')
    def __str__(self):
        return self.nombre


# ========== ===========

class rango_precios(models.Model):
    categoria_presta = models.IntegerField()
    categoria_ml = models.IntegerField()
    cantidad_pack = models.IntegerField()
    cantidad_minima = models.IntegerField()
    cantidad_maxima = models.IntegerField()
    #material = models.ForeignKey(Materiales, blank=True, related_name="material_id_ran", on_delete=models.CASCADE)
    porcetaje = models.FloatField()
    def __str__(self):
        tmp =  '{} - hasta - {} - preta ({}) | ml ({}) '.format(self.cantidad_minima,
                                                                self.cantidad_maxima,
                                                                  self.categoria_presta,
                                                                  self.categoria_ml)
        return tmp

class porcentaje_por_rango(models.Model):
    categoria_presta = models.IntegerField()
    categoria_ml = models.IntegerField()
    peso_minimo = models.FloatField()
    peso_maximo = models.FloatField()
    porcentual = models.FloatField()
    def __str__(self):
        return '{} <-a-> {} : {}%'.format(self.peso_minimo, self.peso_maximo, round((self.porcentual-1)*100,0))


class canales_pago(models.Model):
    nombre = models.CharField(max_length=20)
    porcentaje = models.FloatField()
    def __str__(self):
        return self.nombre
