from .models import (Producto,
                     rango_precios,
                     porcentaje_por_rango,
                     Materiales,
                     canales_pago)



def CalcularPrecios():
    productos = Producto.objects.all()
    lista_final = {}
    lista_final_mp =  {}
    lista_final_ml =  {}
    canal_pago = canales_pago.objects.all()
    pago_ml = canal_pago.filter(nombre__exact='MercadoLibre')[0].porcentaje
    pago_efe = canal_pago.filter(nombre__exact='Efectivo')[0].porcentaje
    pago_mp = canal_pago.filter(nombre__exact='MercadoPago')[0].porcentaje
    index = 0
    for item in productos:
        cantidad_de_piezas= 1000 / float(item.peso)
        precio_unitario = item.material.costo / cantidad_de_piezas
        porcentual  = 0
        porc = porcentaje_por_rango.objects.filter(peso_minimo__lte = item.peso, peso_maximo__gte = item.peso)[0]
        precio_mayor = round(precio_unitario * porc.porcentual,1)
        #Ya obtuvimos el precio por mayor comenzamos a armar el listado.
        tabla_rangos = rango_precios.objects.filter(categoria_presta__exact=item.categoria.categoria_presta)
        lista_temporal = {}
        lista_temporal_ml = {}
        lista_temporal_mp = {}
        for rango in tabla_rangos:
            precio_unitario = round(rango.porcetaje * precio_mayor, 1)
            indice = '{}-{}'.format(rango.cantidad_minima,rango.cantidad_maxima)
            tmp  =  {'Minimo' : rango.cantidad_minima,
                               'Maximo' : rango.cantidad_maxima,
                               'Precio_Libre' : precio_unitario * pago_efe,
                               'Precio_MercadoPago'  : round(precio_unitario * pago_mp,1),
                               'Precio_MercadoLibre' : round(precio_unitario * pago_ml ,1),
                                }
            lista_temporal[indice] =  round(precio_unitario * pago_efe,1)
            lista_temporal_ml[indice] = round(precio_unitario * pago_ml,1)
            lista_temporal_mp[indice] = round(precio_unitario * pago_mp,1)
        lista_final[item.nombre] = lista_temporal
        lista_final_ml[item.nombre] = lista_temporal_ml
        lista_final_mp[item.nombre] = lista_temporal_mp
        index +=1
    return lista_final, lista_final_ml, lista_final_mp



    
    #for item in productos:
    #    print(item.nombre + ' ' )
    #    print(valor.recuperar_tabla_precios(float(item.peso), 16)