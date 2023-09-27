#definiendo una variable
nombre = "tomas"

#concatenar con +
bienvenida = "Hola " + nombre + " ¿como estas?"
print(bienvenida)

#concatenar con f-strings
bienvenida = f"Hola {nombre} ¿como estas?"

#operadores de pertenencia (in / not in)
print("tomas" in bienvenida) #true
print("tomas" not in bienvenida) #false
print(bienvenida)