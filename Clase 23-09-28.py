#       Creando alfabeto aleatorio para llave
import random

def alfabeto_aleatorio(alfabeto): #va a revolvier cualquier alfabeto que le demos
    alfabeto2 = ''
    while len(alfabeto2) < len(alfabeto):
        ale = random.choice(alfabeto)
        if not (ale in alfabeto2):
            alfabeto2 += ale
    return alfabeto2

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
miLlave = alfabeto_aleatorio(alfabeto)
print (miLlave)

def carga_palabras():
    archivo = open('words.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    print(len(palabras), ' palabras leidas')
    return palabras

dic = carga_palabras()

texto = "l prq r yevrz gvvxvdq. Od selqrt "\
        "rszvedood, l sldlupvq goex rz 5 ai "\
        "l gvdz poiv rdq zoox r upogue "\
        "zpvd l gvdz zo uvv r kocabv "\
        "os it selvdqu rz r hre qogdzogd"      

alfabeto = 'xabcdefghijklmnopqrstuvxyz'
frecuencias = {}

for c in alfabeto:
    frecuencias [c] = 0
print()

for e in texto:
    if e in alfabeto:
        frecuencias[e] += 1 # += suma 1
print(frecuencias)

#   Decifrando sin llave
#   qogdzogd - contamos la cnatidad de letras

c = 0
for p in dic:
    if len(p) == 8:
        if (p[2] == p[6]) and (p[1] == p[5]) and (p[3] == p[7]): #buscamos palabras que tengan coincidencias
            print(p)
            c += 1
print(c)

posG = 'ctnwi'
posD = 'kengt'
posQ = 'bcdjmpstw'
posO = 'aoie'

#   goex
c = 0
for p in dic:
    if len(p) == 4:
        if (p[1] in posO) and (p[0] in posG):
            c += 1
print(c)




