diccionario = {
    "nombre" : "Tomas",
    "apellido" : "Roman",
    "edad" : 19
}

#Devuelve un objeto dict_item
claves = diccionario.keys()

#Devuelve un elemento get () (si no encuentra nada , el programa continua)
valor_de_apellido = diccionario.get("apellido")

#Elimina todo el diccionario
#diccionario.clear()

#Elimina un elemento del diccionario
diccionario.pop("apellido")

#Obtener un elemento dict_item iterable (los items son el conjunto de una key-value)
diccionario_iterable = diccionario.items()


print(valor_de_apellido)