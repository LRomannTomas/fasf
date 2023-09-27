#Creando las listas
frutas = ["manzana" , "banana" , "pera" , "ciruela" , "naranja" , "durazno" , "kiwi"]
cadena = "Hola Tomas"
numeros = [2 , 4 , 5 , 7 , 8]
#Evitando que se coma una fruta con la sentencia "continue"
for fruta in frutas:
    if fruta == "pera":
        continue
    print(f"me voy a comer una {fruta}")

#Evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco despues de un break)
for fruta in frutas:
    if fruta == "naranja":
        break
    print(f"me voy a comer una {fruta}")
else: 
    print("bucle terminado")

#recorrer (iterar) una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de código
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
