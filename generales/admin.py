from django.contrib import admin
from .models import (Materiales,
                     Categoria,
                     Producto,
                     rango_precios,
                     porcentaje_por_rango,
                     canales_pago)

admin.site.register(Materiales)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(rango_precios),
admin.site.register(porcentaje_por_rango)
admin.site.register(canales_pago)
