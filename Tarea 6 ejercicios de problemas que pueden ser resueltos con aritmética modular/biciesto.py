def bisiesto(anio):
    cuatro = anio % 4
    cien = anio % 100
    cuatrocientos = anio % 400
    dosmil = anio % 2000
    if(cuatro == 0 and cien != 0) or (cuatro == 0 and cien == 0 and
                                      cuatrocientos == 0 and dosmil == 0):
        return "Es bisiesto"
    else:
        return "No es bisiesto"

print(bisiesto(1904))
print(bisiesto(1900))
print(bisiesto(1908))
print(bisiesto(1996))
print(bisiesto(2000))
print(bisiesto(2001))
print(bisiesto(1904))
print(bisiesto(2004))
