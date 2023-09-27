#Crear una lista con list()
lista = list([ 88, 25, 14, 9898, True])
lista_1 = list([ 88, 25, 14, 9898, True])
lista_2 = list([ 88, 25, 14, 9898, True])

#Devuelve la cantidad de elementos de la lista
resultado = len(lista)

#Agrega un elemento a la lista
lista.append(3)

#Agrega un elemento a la lista en un indice específico y corre al resto a un indice mayor,
lista_2.insert(2, 56)

#Agrega varios elementos a la lista
lista_1.extend([1978, 2023, False])

#Encuentra el indice en el que se encuentra el elemento
lista.index(14)

#Eliminando un elemento de la lista (por su indice)
lista.pop(4) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente 

#Removiendo un elemento de la lista por su valor
lista.remove(3)

#Elimina todos los elementos de la lista
lista.clear()

#Ordenando la lista de forma ascendente (si usamos el parametro reverse = True lo ordena en reversa)
lista.sort()

#Invirtiendo los elementos de una lista
lista.reverse()


print(lista_2)