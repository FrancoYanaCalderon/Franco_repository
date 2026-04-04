#diccionarios -> almacen a pares de clave-valor
mi_diccionario = {'nombre':'Franco Yana', 'edad':25, 'ciudad':'La Paz'}
print(mi_diccionario)

#acceder a iun valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])

#agregar elementos
mi_diccionario['profesion'] = 'ingeniero'
print(mi_diccionario)

#eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

#obtener claves del diccionario
print(mi_diccionario.keys())

#obtener valores del diccionario
print(mi_diccionario.values())
if 'edad' in mi_diccionario:
    print("clave encontrada")
    
#recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[clave: ]"+clave+"[valor:] "+valor)