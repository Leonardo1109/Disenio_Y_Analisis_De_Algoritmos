#                           diccionario en python

# a = {} // con las llaves python ya sabe que es un diccionario
# diccionarios parecidos a las listas.
# a = {}        b = []
# agregando un elemento a la lista b.append("lunes")  b.append("martes")

# agregando un elemento al diccionario debemos tener el valor y la llave
# a["primero"] = "lunes"   a["segundo"] = "martes"
# a["primero"] -> 'lunes'       b[0] -> 'lunes'


#           CREANDO DICCIONARIO POR SUSTITUCION

def cifraSustitucion(cad, llave):
    alfabeto = 'abcdefghijklmnopqrstuvxyz'
    cad = cad.lower() #convierte el exto a minusculas
    cifrado = ''
    for c in cad:   #para cada caracter en la cadena
        if c in alfabeto:   #si el caracter esta en el alfabeto
            pos = alfabeto.index(c)
            cifrado = cifrado + llave[pos]
        else:
            cifrado = cifrado + c
    return cifrado

miAlfabeto = 'cfhjlmgxbatzusyonpvdeqriwk'

a = 'este es un texto de prueba un poco mas grande'\
        'para poder ejercitar algunas estructuras de datos'\
        'tales como el diccionario, y tambien hacer un'\
        'ataque por analisis de frecuencias'
textoCifrado = cifraSustitucion(a, miAlfabeto)

b = cifraSustitucion(a, miAlfabeto)
print (b)
alfabeto = 'abcdefghijklmnopqrstuvxyz'
frecuencias = {}

for c in alfabeto:
    frecuencias [c] = 0
    print (frecuencias)
print()

for e in textoCifrado:
    if e in alfabeto:
        frecuencias[e] += 1 # += suma 1
print(frecuencias)
