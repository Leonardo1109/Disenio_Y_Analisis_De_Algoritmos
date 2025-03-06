def calcula_dia(inicio, conteo):
    inicio = inicio % 7
    dias = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes",
            "sabado"]
    num = ((inicio + conteo) % 7)
    print("El dia que escogió fue: ", dias[inicio], ", avanzando ", conteo)
    return dias[num]

print (calcula_dia(0,0))
print (calcula_dia(0,1))
print (calcula_dia(0,2))
print (calcula_dia(0,3))
print (calcula_dia(0,4))
print (calcula_dia(3,4))
