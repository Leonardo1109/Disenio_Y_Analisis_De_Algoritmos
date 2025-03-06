'''                         Cifrado con funciones                           '''

'''
primer codigo


def cifraCesar(cad, llave): # recibimos la cadena y la llave
    cifrado = ""
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    for c in cad: #Recorremos cada caracter de la cad que nos dieron en la funcion
        print(c) #Imprimimos el caracter
    return cifrado

print(cifraCesar('hola',2))
'''

'''
segundo codigo. Ahora si codificar

def cifraCesar(cad, llave):
    cifrado = ""
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    for c in cad: 
        pos = alfabeto.index(c) #Obtenemos la posicion del alfabeto
        cifrado=cifrado+alfabeto[pos+llave] #En la posicion del alfabeto, le sumamos la llave
    return cifrado

print(cifraCesar('hola',2))

#'hola'.capitalize() = Hola
#'hola'.upper() = HOLA
#'HoLA'.lower() = hola

'''

'''
tercer codigo. Solucionando problemas de mayuscula

def cifraCesar(cad, llave):
    cifrado = ""
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    cad=cad.lower() #para evitar problemas con mayusculas las hacemos minisculas
    for c in cad:
        if c in alfabeto:
            pos = alfabeto.index(c)
            cifrado=cifrado+alfabeto[pos+llave]
        else:
            cifrado += c # Solo agragamos c al cifrado
    return cifrado

print(cifraCesar('HolA - munDO',8))
print(cifraCesar('Zorro',1)) # z se sale de rango
'''


#Tercer codigo, solucionando problemas de fueras de rango (Z)

def cifraCesar(cad, llave):
    cifrado = ""
    alfabeto='abcdefghijklmnopqrstuvwxyz'
    cad=cad.lower()
    for c in cad:
        if c in alfabeto:
            pos = alfabeto.index(c)
            cifrado=cifrado+alfabeto[(pos+llave)%len(alfabeto)]
        else:
            cifrado += c
    return cifrado

print(cifraCesar('HolA - munDO',8))
print(cifraCesar('Zorro',1))


#Funcion que descifra
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

a="Hola mundo"
print(a)
b=cifraCesar(a,8)
print(b)
print(descifraCesar(b,8))

x="tnwfhl vasl s mhvhl"

for llave in range(27):
    print(descifraCesar(x,llave),llave, "c:")



