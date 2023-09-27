#Creando bucle con animales
animales = {"gato", "perro" , "pajaro" , "pez"}

for animal in animales:
    print(animal)

#Creando bucles con numeros 
numeros = {2 , 4 , 6 , 8}

#iterando dos conjuntos del mismo tamaño al mismo tiempo
for numero, animal in zip(animales,numeros):
    print(f"recorriendo conjunto 1: {numero}")
    print(f"recorriendo conjunto 2: {animal}")

#forma correcta de recorrer un conjunto con su inidice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es : {indice} y el valor es {valor}")

for num , i in enumerate(numeros):
    print(f"el indice es: {num} y el valor es: {i}")

#Utilizando el for/else
for number in numeros:
    print(f"ejecutando el ultimo bucle, valor actual : {number}")
else:
    print("el bucle termino")

#Todo lo anterior funciona exactamente igual para tuplas, listas y conjuntos