import random

def cargaPalabras():
    archivo = open('words.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras

def cargaCifrado():
    archivo = open('cifrado.txt', 'r')
    renglon = archivo.readline()    
    return renglon
def descifraSustituye(cadena, alfabetoLlave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'    
    nuevaCadena = ""    
    for letra in cadena:
        if letra in alfabeto:
            posicion = alfabetoLlave.find(letra)
            nuevaCadena = nuevaCadena + alfabeto[posicion]
        else:
            nuevaCadena = nuevaCadena + letra
    return nuevaCadena
dic = cargaPalabras()
cifrado = cargaCifrado()

c = 0
#probando con qogdzogd
for p in dic:
    if len(p) == 8:
        if p[1] == p[5] and p[3] == p[-1] and p[2] == p[6]:
            c = c + 1
            print (p)
print(c)
