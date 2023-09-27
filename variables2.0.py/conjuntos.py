#creando un conjunto con set()
conjunto = set(["dato1",])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1" , "dato 2"])
conjunto2 = {conjunto1 , "dato 3"}

print(conjunto2)

#teoria de conjuntos
conjunto1 = {1 , 3 , 5 , 7}
conjunto2 = {1, 3 , 7} 

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)       #forma 1

resultado = conjunto2 <= conjunto1              #forma 2

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)     #forma 1

resultado = conjunto2 >= conjunto1              #forma 2

#verificar si existe algun número en común
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)