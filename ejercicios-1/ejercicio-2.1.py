
def obtener_compañeros(catidad):
    compañeros = []
    for i in (cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre , edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])





#lista_de_edades = [19, 33, 15, 23, 25, 20]
#lista_de_edades.sort()
#print(lista_de_edades)