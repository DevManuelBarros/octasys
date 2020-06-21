from prestapi import Prestapi

objeto = Prestapi(host="cristalgrafargentina.com/", 
                           protocol="https", 
                        key="4KUR3FXBD5TD9ZJJGXDW9W6B6P1TR72I")

#obj.filter_params(id_field='id', id_value='[full]')
#obj.display_params('id,name')
#obj.set_params_get(resource='manufacturers',display_full=True)
#obj.define_json()
#tmp = obj.executeRequest()
#print(tmp.text)

#objeto.set_params_get(resource='countries')
#objeto.filter_params(id_field='id',id_value='[10,25]', display='id,name,active')
#objeto.define_json() # devolvera un elemento Json
#objeto.define_json(type_json=False)   #devolvera un elemento tipo Xml
#result = tmp = objeto.executeRequest() #ejecutaremos la consulta.
#print(result.text)

#result = objeto.delete(resource='addresses', id=11)

#print(result[1])
#result = objeto.search(resource='addresses', display='id,lastname')
#print(result.text)


#obj.set_params_get(resource="warehouses", schema='blank')
#tmp = obj.executeRequest()


#tmp = obj.add_get(resource="addresses",rec_id=False)

#tmp['struct']['alias']  = 'daisdoisad'
#tmp['struct']['lastname'] = 'DOEs'
#tmp['struct']['firstname'] = 'dsdads'
#tmp['struct']['address1'] = 'Una ddireccion'
#tmp['struct']['postcode'] = '0123456'
#tmp['struct']['city'] = 'Paris'
#tmp['struct']['id_country'] = 1 

#tmp = obj.get_id_name('customers', 'lastname,firstname')
#print(tmp['rules'])
#print(dicttoxml.dicttoxml(tmp['struct'],custom_root='some_custom_root'))

#result = obj.add('addresses',tmp)
#print(result)
#soto = obj.get_id_name('addresses', 'alias,postcode,id_country')
#print(soto)


#tmp = objeto.add_get('products')
#tmp = objeto.add_get('products', rec_id=False)
#print(tmp)
"""
tmpResult = objeto.get_struct('addresses')

tmpResult['address']['alias']  = 'Direccion1'
tmpResult['address']['lastname'] = 'Unapellido'
tmpResult['address']['firstname'] = 'Unnombre'
tmpResult['address']['address1'] = 'Una direccion'
tmpResult['address']['postcode'] = '1234567'
tmpResult['address']['city'] = 'Buenos Aires'
tmpResult['address']['id_country'] = 1 
print(tmpResult)
#tea = objeto.delete(resource='addresses', id=13)
#print(tea)


result = objeto.save(resource='addresses', data=tmpResult)
print(result.text)
tp = objeto.search(resource='addresses', display='id,alias')
print(tp.text)
"""
"""
result_get = objeto.add_get(resource='addresses')

result_get['struct']['alias']  = 'Direccion2'
result_get['struct']['lastname'] = 'Otropellido'
result_get['struct']['firstname'] = 'Otronombre'
result_get['struct']['address1'] = 'dos direccion'
result_get['struct']['postcode'] = '2345678'
result_get['struct']['city'] = 'Santa Fe'
result_get['struct']['id_country'] = 1 
print(result_get['struct'])

resultado = objeto.add(result_get, comp_dat=True)
print(resultado.text)
"""

resultado = objeto.put_get(resource='addresses', id=14)
print(resultado)
resultado['addresses']['firstname'] = 'NuevoPrimerNombre'
final = objeto.put(resultado)
print(final.text)
