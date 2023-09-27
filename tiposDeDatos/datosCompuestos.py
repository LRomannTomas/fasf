lista = ["tomas roman", "Soy tomas" , True,1.82] #Sirve para agrupar un conjunto de datos que se pueden modificar.

tupla = ("tomas roman", "Soy tomas" , True,1.82) #Sirve para agrupar un conjunto de datos que nunca se van a modificar.

#Esto es valido!
lista[2] = False 

#Esto no es valido!
#tupla[0] = "roman tomas" 

#Creando un conjunto (set)
conjunto = {"tomas roman", "Soy tomas" , True,1.82,"Soy tomas"} #En un conjunto no pueden haber datos duplicados por mas que se intenten crear; no se accede a elementos por indice.

#print(conjunto[2]) --> no se puede acceder al elemento

#Creando un diccionario (dict) (la estructura es key : value y se separa con comas)
diccionario = {
    "nombre" : "tomas roman",
    "edad" : 19,
    "se_siente_bien" : True,
    "altura" : 1.82,   
    "dato_duplicado" : "Soy tomas"
}

print(diccionario["dato_duplicado"])
