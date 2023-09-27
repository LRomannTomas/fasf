cadena1 = "Es,Un,Dia,Lluvioso"
cadena2 = "Hola Soy Tomas"

#Convierte a mayusculas
mayusculas = cadena2.upper()

#Convierte a minisculas
minusculas = cadena2.lower()

#Primera letra en mayuscula
primer_letra_mayus = cadena2.capitalize()

#Convierte la primera letra en mayuscula de todos los textos
todas_primer_letra_mayus = cadena2.title()

#Buscar una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena2.find("T")

#Buscar una cadena en otra cadena, si no hay coincidencias devuelve una excepcion
busqueda_index = cadena2.index("T")

#Si es numerico devuelve True, si no devuelve False
es_numerico = cadena1.isnumeric()

#Si es alfanumerico devuelve True, si no devuelve False (Los caracteres alfanumericos son solo las letras A-Z, excluyendo tambien a los espacios)
es_alfanumerico = cadena1.isalpha()

#Busca las coincidencias de una cadena, dentro de otra cadena, deuelve la cantidad de coincidencias encontradas
contar_coincidencias = cadena1.count("a")

#Cuenta los caracteres que tiene una cadena
contar_caracteres = len(cadena1)

#Verifica si una cadena comienza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("a")

#Verifica si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("f")

#Si el valor 1 de la cadena original se encuentra, lo remplaza por el valor 2
cadena_nueva = cadena1.replace("," , " ")

#Separa cadenas con la cadena que le otorguemos
cadena_separada = cadena1.split(",")


print(minusculas)

