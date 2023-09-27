persona_promedio = 1 / 2

peticion = input(" -- Introduci el texto que quieras: ")
contador = peticion.split(" ")
cantidad_de_palabras = len(contador)
cuenta = len(contador) / 2

if cuenta > 120 :
    print(" - Para flaco tampoco te pedi un testamento")
elif cuenta < 120 :
    print(f" - Dijiste {cantidad_de_palabras} palabras y tardarias en decir este texto " ,cuenta, "segundos")

print(f" - Dalto tardaria {cantidad_de_palabras // 2 * 0.7} segundos en decirlo")

