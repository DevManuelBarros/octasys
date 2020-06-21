from django.db import models


class PrestaConfig(models.Model):
    OP_PROTOCOL = (
                    ('http', 'http'),
                    ('https', 'https'), 
                  )
    name = models.CharField(max_length=20, 
                            unique=True,
                            blank=False,
                            help_text="Nombre identificador de la configuración del sitio que contiene la API")
    host = models.CharField(max_length=150, 
                            blank=False, 
                            help_text="Host donde se aloja la API, ejemplo: localhost.com")
    protocol = models.CharField(max_length=10, 
                                choices=OP_PROTOCOL, 
                                blank=False,
                                default='http',
                                help_text="Protocolo por el cual el host responde.")
    key = models.CharField(max_length=50,
                           blank=False,
                           help_text="Key generada por la API de Prestashop.")
    active = models.BooleanField(help_text="Si el registro se encuentra activo.")
    default = models.BooleanField(default=False, blank=False, help_text='El campo que este en true será el que se tome.')    
    
    def __str__(self):
        return self.name
