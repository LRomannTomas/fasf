ingreso_mensual = 10000
gasto_mensual = 7000

if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual > 6000:
        print("Estas bien en cualquier parte del mundo")
    elif ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    else:
        print("Estas gastando mucho dinero")

elif ingreso_mensual >= 7000:
    print("Estas medianamente bien en cualquier parte del mundo")

elif ingreso_mensual >= 5000:
    print("Estas bien economicamente en LatinoAmerica")

else: 
    print("sos pobre xd")