""" PROBLEMAS NP (No polimoniales)
    PROBLELMA KHAPSACK: Tiene un costo de 2^n (Posible resolver solo con 30 elementos)
    Problema del agente viajero: Tiene un costo de n! (Posible resolver solo 15 elementos)

    ¿Podriamos encontrar una aproximacion para pasar un problema NP a P?
    
"""
"""
# -- coding: cp1252 --
import time
class Cosas():
    nombre = ""
    precio = 0
    peso = 0
    llevado = 0
    valor = 0.0
##  El valor será obtenido dividiendo el precio entre el peso
    def _init_(self, nom, pre, pes, llev):
        self.nombre = nom
        self.precio = pselfre
        self.peso = pes
        self.llevado = llev
        self.valor = pre/pes

def evalua(num, arregloCosas, restriccion):
    pos=0
    ganancia=0
    peso=0
    cad = bin(num)
    cad = cad[2:]
    cad = cad.rjust(len(arregloCosas))
    cad = cad.replace(" ","0")
    for l in cad:
        if l == "1":
            ganancia += arregloCosas[pos].precio
            peso += arregloCosas[pos].peso
        pos+=1
    if peso > restriccion:
        return -1
    else:
        return ganancia

def imprimeCombinacion(num):
    pos=0
    ganancia=0
    peso=0
    cad = bin(num)
    cad = cad[2:]
    cad = cad.rjust(len(arregloCosas))
    cad = cad.replace(" ","0")
    print()
    print ("           La mejor combinacion es   ")
    print ("objeto  Precio    peso")
    for l in cad:
        if l == "1":
            texto =arregloCosas[pos].nombre + "    "
            texto = texto + str(arregloCosas[pos].precio)+"         "
            texto = texto + str(arregloCosas[pos].peso)
            print (texto)
            ganancia += arregloCosas[pos].precio
            peso += arregloCosas[pos].peso
        pos+=1
    print ()
    print ("Ganancia total: "+ str(ganancia)+ "  Peso total: "+str(peso))

arregloCosas=[]

arregloCosas.append(Cosas('cuaderno',20,2,0))
arregloCosas.append(Cosas('libro',10,1,0))
arregloCosas.append(Cosas('Licuadora',100,10,0))
arregloCosas.append(Cosas('Pintura',200,18,0))
arregloCosas.append(Cosas('STEREO',150,13,0))
arregloCosas.append(Cosas('computadora',200,16,0))
arregloCosas.append(Cosas('Microondas',200,15,0))
arregloCosas.append(Cosas('sombrilla',40,3,0))
arregloCosas.append(Cosas('Calculadora',103,6,0))
arregloCosas.append(Cosas('Botas',89,5,0))
arregloCosas.append(Cosas('Balon',54,3,0))
arregloCosas.append(Cosas('JARRON',38,2,0))
arregloCosas.append(Cosas('Cuadro',100,5,0))
arregloCosas.append(Cosas('Maleta',100,5,0))
arregloCosas.append(Cosas('Radio',180,9,0))
arregloCosas.append(Cosas('Silla',240,12,0))
arregloCosas.append(Cosas('TELEFONO',20,1,0))
#arregloCosas.append(Cosas('Xbox',369,15,0))
#arregloCosas.append(Cosas('florero',50,2,0))
#arregloCosas.append(Cosas('Luces',50,2,0))
#arregloCosas.append(Cosas('Estereo',340,13,0))
#arregloCosas.append(Cosas('Celular Nokia',28,1,0))
#arregloCosas.append(Cosas('Guitarra',450,16,0))
##arregloCosas.append(Cosas('Wii',346,12,0))
##arregloCosas.append(Cosas('Sombrero',60,2,0))
##arregloCosas.append(Cosas('reloj',110,3,0))
##arregloCosas.append(Cosas('VAJILLA',160,4,0))
#arregloCosas.append(Cosas('Los relojes Blandos. Dalí',250,6,0))
##arregloCosas.append(Cosas('Calendario Maya',456,9,0))
##arregloCosas.append(Cosas('DVD',110,2,0))
#arregloCosas.append(Cosas('Busto Platón',300,10,0))
##arregloCosas.append(Cosas('Adorno',70,3,0))


## Esta parte corresponde a la búsqueda exhaustiva
inicio = time.time()
print ("Probando con búsqueda exahustiva")
maximo = 0
mejorCombina = 0
for c in range(pow(2,len(arregloCosas))):
    obtenido = evalua (c, arregloCosas, 20)
    if obtenido > maximo:
        maximo = obtenido
        mejorCombina = c
imprimeCombinacion(mejorCombina)
fin = time.time()
tiempo = fin-inicio
print("tiempo requerido = ", tiempo, " segundos")
## Fin de la búsqueda exhaustiva
"""

class Ciudad:
    def __init__(self, numero, x, y, visitada):
        self.numero = numero
        self.x = x
        self.y = y
        self.visitada = visitada

#Funcion que calcula distancia
import math
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print (distancia(2,2,5,6))


#Funcion que crea ciudades al azar
import random
def crea_ciudades_ale(n):
    ciudades = []
    for c in range (n):
        x_ale = random.randint(0,100)
        y_ale = random.randint(0,100)
        ciudades.append(Ciudad(c, x_ale, y_ale, False))
    return ciudades

ciudades = crea_ciudades_ale(20)

ciudades[0].visitada = True

#Funcion que busca la ciudad mas cerca
def ciudad_mas_cerca(actual, lista):
    if actual == 0:
        mejorCiudad = 1
    else:
        mejorCiudad = 0
    for c in range (len(ciudades)):
        if ciudades[c].visitada == False:
            print (c, distancia(ciudades[actual].x, ciudades[actual].y,
                          ciudades[c].x, ciudades[c].y))
            if distancia(ciudades[actual].x, ciudades[actual].y, ciudades[c].x,
            ciudades[c].y) < distancia(ciudades[actual].x,
            ciudades[actual].y, ciudades[mejorCiudad].x,
            ciudades[mejorCiudad].y):
                mejorCiudad = c
    ciudades[mejorCiudad].visitada = True
    return mejorCiudad, distancia(ciudades[actual].x, ciudades[actual].y,
                          ciudades[mejorCiudad].x, ciudades[mejorCiudad].y)

print (ciudad_mas_cerca(0,ciudades))

"""
    recorrrido = []
    actual = 0
    recorrido.append(actual)
    cercana = get_mas_cercana(actual, ciudades)
    ciudades[actual].visitada = True
    recorrido.append(actual)
    actual = cercana
"""
###############################################################################
"""
EXAMEN 16 DE NOVIEMBRE | CODIGO

Examen ejercicios y teoria de cadenas en python; listas; funciones (.lower; upper; ordenar; añadir;
                                                                    rebanadas** a[2:2])
Ejercicios con funciones | Problemas P y NP | Ejemplos de tipo O(n!); O(2^n) o decir que tipo de costo es
Problemas de aritmetica modular
"""

"""
Proyecto: cifrdo (Italino; frances; ingles y probblemente portuges y aleman)
"""










