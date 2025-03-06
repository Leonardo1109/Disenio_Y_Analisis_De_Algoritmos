"""
costo de busqueda en arbol binario = log_2(n)
costo de  ordenar o crear un arbol binario = n log(n)

0(1) meter o sacar de una pila
0(n) recorrer un areglo
0(n log (n)) quicksort
0(n^2) metodo ordenmiento burbuja
0(n!) cifrado por llave alfabetica sustituida
"""

"""
#creando una funcion para calcular n!
def factorial_recursivo(valor):
    print("trabajando con valor ", valor) #cuantas veces se manda a llamar
    if valor==0:
        return 1
    else:
        return valor*factorial_recursivo(valor-1) #5*4! -> 5*4*3! -> 5*4*3*2! ..
print(factorial_recursivo(5))
"""

"""
#nueva funcion para n! usando factorial iterativo (for)
def factorial_iter(n):
    print("trabajando con valor ", n) #solo se manda a llamar un vez
    resultado = 1
    for c in range (1, n+1):
        resultado = resultado * c
    return resultado
print(factorial_iter(5))
"""

def es_palin1(cad):
    cad1=""
    for c in cad:
        cad1 = c + cad1
    return cad==cad1
print(es_palin1("aibofobia"))

def es_palin2(cad):
    if (len(cad)==0) or (len(cad)==1):
        return True
    else:
        return (cad[0] == cad[-1]) and es_palin2(cad[1:-1])
print(es_palin2("aibofobia"))

def es_palin3(cad):
    return cad==cad[::-1]
print(es_palin3("oso"))

# a=abcedefghijklmn
# a[8:3:-2] 1° es donde empezamos, 2° donde termina la cadena, 3° saltos
# a[8:3:-2] 1° i; 2° e; 3° i, g, e
# cad[::-1] empieza en 0, termina en leng, va saltando hacia atras

