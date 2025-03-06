# funcion para obtener las palabras del diccionario Ingles separadas
def cargaPalabrasIngles():
    with open('diccionarioIngles.txt', 'r') as archivo: 
        renglon = archivo.readline()
        palabrasIngles = renglon.split()
        return palabrasIngles

# funcion para obtener las palabras del diccionario Frances separadas
def cargaPalabrasFrances():
    with open('diccionarioFrances.txt', 'r') as archivo: 
        renglon = archivo.readline()
        palabrasFrances = renglon.split()
        return palabrasFrances
    
# funcion para obtener las palabras del diccionario Italiano separadas
def cargaPalabrasItaliano():
    with open('diccionarioItaliano.txt', 'r') as archivo: 
        renglon = archivo.readline()
        palabrasItaliano = renglon.split()
        return palabrasItaliano

# funcion para obtener el texto cifrado
def cargaCifrado():
    with open('textoCifrado.txt', 'r') as archivo:
        renglon = archivo.readline()
    return renglon

# Funcion que cifra en Ingles
def cifraCesarIngles(cadena, llave):
    if llave < 0: # si tenemos una llave menor a 0 se la restamos a 26
        llave = 26 - llave 
    cadena = cadena.lower() # hacemos el texto minusculas
    nuevaCadena = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for l in cadena:
        if l in alfabeto:
            posicionLetra = alfabeto.find(l)
            nuevaCadena = nuevaCadena + alfabeto[((posicionLetra + llave) % 26)]
        else:
            nuevaCadena = nuevaCadena + l # si no se encuentra, deja igual
    return nuevaCadena

# Funcion que descifra en Ingles
def descifraCesarIngles(cadena, llave):
    return cifraCesarIngles(cadena, 26 - llave)

# Funcion que cifra en Frances
def cifraCesarFrances(cadena, llave):
    if llave < 0: # si tenemos una llave menor a 0 se la restamos a 25
        llave = 25 - llave 
    cadena = cadena.lower() # hacemos el texto minusculas
    nuevaCadena = ""
    alfabeto = "abcdefghijklmnopqrstuvxyz" #falta w
    for l in cadena:
        if l in alfabeto:
            posicionLetra = alfabeto.find(l)
            nuevaCadena = nuevaCadena + alfabeto[((posicionLetra + llave) % 25)]
        else:
            nuevaCadena = nuevaCadena + l # si no se encuentra, deja igual
    return nuevaCadena

# Funcion que descifra en Frances
def descifraCesarFrances(cadena, llave):
    return cifraCesarFrances(cadena, 25 - llave)

# Funcion que cifra en Italiano
def cifraCesarItaliano(cadena, llave):
    if llave < 0: # si tenemos una llave menor a 0 se la restamos a 23
        llave = 23 - llave 
    cadena = cadena.lower() # hacemos el texto minusculas
    nuevaCadena = ""
    alfabeto = "abcdefghijlmnopqrstuvxz" # Falta kwy
    for l in cadena:
        if l in alfabeto:
            posicionLetra = alfabeto.find(l)
            nuevaCadena = nuevaCadena + alfabeto[((posicionLetra + llave) % 23)]
        else:
            nuevaCadena = nuevaCadena + l # si no se encuentra, deja igual
    return nuevaCadena

# Funcion que descifra en Italiano
def descifraCesarItaliano(cadena, llave):
    return cifraCesarItaliano(cadena, 23 - llave)

def getAciertos(listaPalabras, diccionario):
    numAciertos = 0
    for pal in listaPalabras: # le damos un conjunto de palabras
        if pal in diccionario: # si la palabra esta en el diccionario, acierto
            numAciertos = numAciertos + 1 
    return numAciertos

maxAciertos = 0
mejorllave = 0
mejorIdioma = ""

def descifraAutomaticoIngles():
    for llave in range(27): # Probamos con cada llave REVISAR SI ES 27
        prueba = descifraCesarIngles(cargaCifrado(), llave)
        #obtenemos los posible acierto en el dic
        aciertos = getAciertos(prueba.split(), cargaPalabrasIngles())
        if aciertos > maxAciertos: # si es mayor, es posible que sea la llave
            maxAciertos = aciertos
            mejorllave = llave # actualizamos
            mejorIdioma = "Ingles"

def descifraAutomaticoFrances():
    for llave in range(26): # Probamos con cada llave 
        prueba = descifraCesarFrances(cargaCifrado(), llave)
        #obtenemos los posible acierto en el dic
        aciertos = getAciertos(prueba.split(), cargaPalabrasFrances())
        if aciertos > maxAciertos: # si es mayor, es posible que sea la llave
            maxAciertos = aciertos
            mejorllave = llave # actualizamos
            mejorIdioma = "Frances"

def descifraAutomaticoItaliano():
    for llave in range(24): # Probamos con cada llave 
        prueba = descifraCesarItaliano(cargaCifrado(), llave)
        #obtenemos los posible acierto en el dic
        aciertos = getAciertos(prueba.split(), cargaPalabrasItaliano())
        if aciertos > maxAciertos: # si es mayor, es posible que sea la llave
            maxAciertos = aciertos
            mejorllave = llave # actualizamos
            mejorIdioma = "Italiano"
            
descifraAutomaticoIngles()
descifraAutomaticoFrances()
descifraAutomaticoItaliano()
print("La mejor llave es: ", mejorllave)
if mejorIdioma == "Ingles":
    print("El texto buscado es: ",
          descifraCesarIngles(cargaCifrado(), mejorllave), "\nEsta cifrado en ",
          mejorIdioma)
elif mejorIdioma == "Frances":
    print("El texto buscado es: ",
          descifraCesarFrances(cargaCifrado(), mejorllave), "\nEsta cifrado en ",
          mejorIdioma)
elif mejorIdioma == "Italiano":
    print("El texto buscado es: ",
          descifraCesarItaliano(cargaCifrado(), mejorllave), "\nEsta cifrado en ",
          mejorIdioma)
    


