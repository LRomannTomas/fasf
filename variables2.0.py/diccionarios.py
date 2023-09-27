#creando  diccionarios con dict()
diccionario = dict(nombre = "Tomas" , apellido = "Roman")

#las listas no pueden ser claves, las tuplas si. Ya que las listas son iterables y las tuplas no.

#diccionario = {["tomas" , "roman"] : "xd"} ---> NO SE PUEDE
diccionario = {("tomas" , "roman") : "xd"}   #---> SI SE PUEDE

#Usamos frozenset para meter conjuntos
diccionario = { frozenset(["tomas" , "roman "]): "xd"}

#creando diccionario con dict.frontkeys () valor por defecto: None
diccionario = dict.fromkeys("ABCD" , "Algun valor fijo")

#creando diccionario con dict.frontkeys () cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre" , "apellido"] , "No se")



print(diccionario)
