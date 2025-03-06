a=[1,3,4,5,6,7]
print(3 in a)
print(2 in a)

b="hola buenos dias a todos en este jueves de septiembre"
#   las cadenas son objetos
print(len(b))
"""
b.split() = ['hola', 'buenos', 'dias', 'a', 'todos', 'en', 'este', 'jueves', 'de', 'septiembre']
parte la cadena por palabras haciendolo una lista
.split() por defecto separa por espacios, pero si queremos algo en especifico
va dentro del parentesis  .split(,)
"""

c = b.split()
print(c)
print(len(c))
print(b[2], c[2])
c.sort() #ordena alfabeticamente la lista de palabras
print(c)

#                           Creando un Diccionario                             #

dic1=["a", "abajo", "arriba", "bacilio"]

#   Encontrar la llave automaticamente del cifrado, descifrado usando un diccionario

#   Funcion que cifra
def cifraCesar(cad, llave):
    cifrado = ""
    alfabeto='abcdefghijklmnñopqrstuvwxyz'
    cad=cad.lower()
    for c in cad:
        if c in alfabeto:
            pos = alfabeto.index(c)
            cifrado=cifrado+alfabeto[(pos+llave)%len(alfabeto)]
        else:
            cifrado += c
    return cifrado

#   Funcion que descifra
def descifraCesar(cad, llave):
    descifrado = ""
    alfabeto='abcdefghijklmnñopqrstuvwxyz'
    cad = cad.lower()
    for c in cad:
        if c in alfabeto:
            pos = alfabeto.index(c)
            descifrado = descifrado + alfabeto[(pos-llave)%len(alfabeto)]
        else:
            descifrado += c
    return descifrado

dic = ["abajo", "arriba", "hambre", "vamonos", "ya"]

#   funcion que comprueba mejor llave
def getAciertos(prueba, dic):
    aciertos = 0
    prueba = prueba.split()
    for e in prueba:
        if e in dic:
            aciertos += 1
    return aciertos

maxAciertos = 0
mejorllave = 0
for llave in range(27):
    prueba = descifraCesar("km hmxayae fpyra smxndp", llave)
    aciertos = getAciertos(prueba, dic)
    if aciertos > maxAciertos:
        maxAciertos = aciertos
        mejorllave = llave
print("La mejor llave es: ", mejorllave)
print("El texto buscado es: ", descifraCesar("km hmxayae fpyra smxndp",mejorllave))



#   con \concatena una cadena NOTA: dejar un espacio despues del siguente salto de linea
a = "esta es una cadena de prueba para un ejercicio en clase"\
    " y queremos crear un pequeño diccionario para una tarea"\
    " donde vamos a quitar palabras repetidas"
b = a.split()
print(len(b))
print(b)

c = [] #lista vacia
for pal in b:
    if not (pal in c):
        c.append(pal)
c.sort()
print(c, '\n', len(c))

#   Conjuntos
d = [1,2,3,5,7,11]
e = [1,3,5,7,9]
f = [1,2,2,1,3,1,2,3,1]
g = set(f) #    Elimina los numeros repetidos
print(g)
f = list(set(f)) #  Equivalente a lo que hicimos anteriormente en la cadena eliminando repetidos
print(f)









