numeros = [1,2,3,4,5,6,7,8,9]

#creando una funcion lamda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#creando una funcion que determine si el numero es par o no
#def es_par(num):
#    if(num % 2 == 0):
#        return True

#usando filter en una funcion comun
#numeros_pares = filter(es_par , numeros)

#creando lo mimsmo que antes pero con lambda
numeros_pares = filter(lambda numero : numero % 2 == 0, numeros)

print(list(numeros_pares))
