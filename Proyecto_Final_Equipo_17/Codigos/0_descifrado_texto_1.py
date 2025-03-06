def cargaPalabras(): # cargamos diccionario
    archivo = open('ingles_diccionario.txt', 'r')
    renglon = archivo.readline()
    palabras = renglon.split()
    return palabras

def cargaCifrado(): # cargamos texto cifrado 1
    archivo = open('texto_1_cifrado.txt', 'r')
    renglon = archivo.readline()    
    return renglon

def descifraSustituye(cadena, alfabetoLlave):
    cadena = cadena.lower()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    nuevaCadena = ""    
    for letra in cadena: # recorre texto
        if letra in alfabeto: # busca la letra en el alfabeto
            posicion = alfabeto.find(letra) # obtiene posicion del alfabeto
            nuevaCadena = nuevaCadena + alfabetoLlave[posicion] # pos nuevo alf
        else:
            nuevaCadena = nuevaCadena + letra # si no esta en alfabeto
    return nuevaCadena

dic = cargaPalabras()
cifrado = cargaCifrado()

"""
posA = 'abcdefghijklmnopqrstuvwxyz' # 0
posB = 'abcdefghijklmnopqrstuvwxyz'
posC = 'abcdefghijklmnopqrstuvwxyz'
posD = 'abcdefghijklmnopqrstuvwxyz'
posE = 'abcdefghijklmnopqrstuvwxyz'
posF = 'abcdefghijklmnopqrstuvwxyz'
posG = 'abcdefghijklmnopqrstuvwxyz'
posH = 'abcdefghijklmnopqrstuvwxyz'
posI = 'abcdefghijklmnopqrstuvwxyz'
posJ = 'abcdefghijklmnopqrstuvwxyz'
posK = 'abcdefghijklmnopqrstuvwxyz'
posL = 'abcdefghijklmnopqrstuvwxyz'
posM = 'abcdefghijklmnopqrstuvwxyz'
posN = 'abcdefghijklmnopqrstuvwxyz'
posO = 'abcdefghijklmnopqrstuvwxyz'
posP = 'abcdefghijklmnopqrstuvwxyz' # 0
posQ = 'abcdefghijklmnopqrstuvwxyz'
posR = 'abcdefghijklmnopqrstuvwxyz'
posS = 'abcdefghijklmnopqrstuvwxyz' # 0
posT = 'abcdefghijklmnopqrstuvwxyz'
posU = 'abcdefghijklmnopqrstuvwxyz'
posV = 'abcdefghijklmnopqrstuvwxyz'
posW = 'abcdefghijklmnopqrstuvwxyz'
posX = 'abcdefghijklmnopqrstuvwxyz'
posY = 'abcdefghijklmnopqrstuvwxyz'
posZ = 'abcdefghijklmnopqrstuvwxyz'
c = 0

#probando con Crzztcc
for p in dic:
    if len(p) == 7:
        if p[0] == p[5] and p[0] == p[6] and p[2] == p[3]:
            c = c + 1
            print(p)
print(c)
# Solo una palabra: success
"""
"""
posA = 'abcdefghijklmnopqrstuvwxyz'
posB = 'abcdefghijklmnopqrstuvwxyz'
posC = 's'
posD = 'abcdefghijklmnopqrstuvwxyz'
posE = 'abcdefghijklmnopqrstuvwxyz'
posF = 'abcdefghijklmnopqrstuvwxyz'
posG = 'abcdefghijklmnopqrstuvwxyz'
posH = 'abcdefghijklmnopqrstuvwxyz'
posI = 'abcdefghijklmnopqrstuvwxyz'
posJ = 'abcdefghijklmnopqrstuvwxyz'
posK = 'abcdefghijklmnopqrstuvwxyz'
posL = 'abcdefghijklmnopqrstuvwxyz'
posM = 'abcdefghijklmnopqrstuvwxyz'
posN = 'abcdefghijklmnopqrstuvwxyz'
posO = 'abcdefghijklmnopqrstuvwxyz'
posP = 'abcdefghijklmnopqrstuvwxyz'
posQ = 'abcdefghijklmnopqrstuvwxyz'
posR = 'u'
posS = 'abcdefghijklmnopqrstuvwxyz'
posT = 'e'
posU = 'abcdefghijklmnopqrstuvwxyz'
posV = 'abcdefghijklmnopqrstuvwxyz'
posW = 'abcdefghijklmnopqrstuvwxyz'
posX = 'abcdefghijklmnopqrstuvwxyz'
posY = 'abcdefghijklmnopqrstuvwxyz'
posZ = 'c'
c = 0

# probando con egddtltmzt
for p in dic:
    if len(p) == 10:
        if p[2] == p[3] and p[4] in posT and p[4] == p[6] and p[4] == p[9]:
            c = c + 1
            print(p)
print(c)
# solo una palabra: difference
"""
"""
posA = 'abhijklmopqtvwxyz'
posB = 'abhijklmopqtvwxyz'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'abhijklmopqtvwxyz'
posG = 'abhijklmopqtvwxyz'
posH = 'abhijklmopqtvwxyz'
posI = 'g' #error 
posJ = 'abhijklmopqtvwxyz'
posK = 'abhijklmopqtvwxyz'
posL = 'r'
posM = 'n'
posN = 'abhijklmopqtvwxyz'
posO = 'abhijklmopqtvwxyz'
posP = 'abhijklmopqtvwxyz'
posQ = 'abhijklmopqtvwxyz'
posR = 'u'
posS = 'abhijklmopqtvwxyz'
posT = 'e'
posU = 'abhijklmopqtvwxyz'
posV = 'abhijklmopqtvwxyz'
posW = 'abhijklmopqtvwxyz'
posX = 'abhijklmopqtvwxyz'
posY = 'abhijklmopqtvwxyz'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['s', 'f', 'd', 'g', 'r', 'n', 'u', 'e', 'c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto)
        
# probando en zbmolbq
for p in dic:
    if len(p) == 7:
        if (p[0] in posZ and p[1] in posB and p[2] in posM and p[3] in posO
            and p[4] in posL and p[1] == p[5] and p[6] in posQ):
            c = c + 1
            print(p)
print(c)
# Nos da 4 resultados asi que usamos el abecedario reducido
# Al usar los abecedarios reducidos obtenemos un resultado: control
"""
"""
posA = 'abhijkmpqvwxyz'
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'abhijkmpqvwxyz'
posG = 'abhijkmpqvwxyz'
posH = 'abhijkmpqvwxyz'
posI = 'g'
posJ = 'abhijkmpqvwxyz'
posK = 'abhijkmpqvwxyz'
posL = 'r'
posM = 'n'
posN = 'abhijkmpqvwxyz'
posO = 't'
posP = 'abhijkmpqvwxyz'
posQ = 'l'
posR = 'u'
posS = 'abhijkmpqvwxyz'
posT = 'e'
posU = 'abhijkmpqvwxyz'
posV = 'abhijkmpqvwxyz'
posW = 'abhijkmpqvwxyz'
posX = 'abhijkmpqvwxyz'
posY = 'abhijkmpqvwxyz'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','g','r','n','t','l','u','e','c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # abhijkmpqvwxyz

# probando en ybytmoc
for p in dic:
    if len(p) == 7:
        if (p[0] in posY and p[1] in posB and p[2] == p[0] and p[3] in posT
            and p[4] in posM and p[5] in posO and p[6] in posC):
            c = c + 1
            print(p)
print(c)
# 1 resultado : moments
"""
"""
posA = 'abhijkpqvwxyz'
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'abhijkpqvwxyz'
posG = 'abhijkpqvwxyz'
posH = 'abhijkpqvwxyz'
posI = 'g'
posJ = 'abhijkpqvwxyz'
posK = 'abhijkpqvwxyz'
posL = 'r'
posM = 'n'
posN = 'abhijkpqvwxyz'
posO = 't'
posP = 'abhijkpqvwxyz'
posQ = 'l'
posR = 'u'
posS = 'abhijkpqvwxyz'
posT = 'e'
posU = 'abhijkpqvwxyz'
posV = 'abhijkpqvwxyz'
posW = 'abhijkpqvwxyz'
posX = 'abhijkpqvwxyz'
posY = 'm'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','g','r','n','t','l','u','e','m','c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # abhijkpqvwxyz

# probando en Gd  
for p in dic:
    if len(p) == 2:
        if (p[0] in posG and p[1] in posD):
            c = c + 1
            print(p)
print(c)
# 1 resultado: if
"""
"""
posA = 'abhjkpqvwxyz' # 0
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'abhjkpqvwxyz'
posG = 'i'
posH = 'abhjkpqvwxyz'
posI = 'g'
posJ = 'abhjkpqvwxyz'
posK = 'abhjkpqvwxyz'
posL = 'r'
posM = 'n'
posN = 'abhjkpqvwxyz'
posO = 't'
posP = 'abhjkpqvwxyz' # 0
posQ = 'l'
posR = 'u'
posS = 'abhjkpqvwxyz' # 0
posT = 'e'
posU = 'abhjkpqvwxyz'
posV = 'abhjkpqvwxyz'
posW = 'abhjkpqvwxyz'
posX = 'abhjkpqvwxyz'
posY = 'm'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','i','g','r','n','t','l','u','e','m',
                         'c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # abhjkpqvwxyz

# probando en yxwblgov  
for p in dic:
    if len(p) == 8:
        if (p[0] in posY and p[1] in posX and p[2] in posW and p[3] in posB
             and p[4] in posL and p[5] in posG and p[6] in posO
             and p[7] in posV):
            c = c + 1
            print(p)
print(c)  
# 1 resultado: majority
"""
"""
posA = 'bhkpqvwxz' # 0
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'bhkpqvwxz'
posG = 'i'
posH = 'bhkpqvwxz'
posI = 'g'
posJ = 'bhkpqvwxz'
posK = 'bhkpqvwxz'
posL = 'r'
posM = 'n'
posN = 'bhkpqvwxz'
posO = 't'
posP = 'bhkpqvwxz' # 0
posQ = 'l'
posR = 'u'
posS = 'bhkpqvwxz' # 0
posT = 'e'
posU = 'bhkpqvwxz'
posV = 'y'
posW = 'j'
posX = 'a'
posY = 'm'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','i','g','r','n','t','l','u','e','y',
                         'j','a','m','c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # bhkpqvwxz

# probando en xqnxvc  
for p in dic:
    if len(p) == 6:
        if (p[0] in posX and p[1] in posQ and p[2] in posN and p[3] in posX
             and p[4] in posV and p[5] in posC):
            c = c + 1
            print(p)
print(c)  
# 1 resultado: always
"""
"""
posA = 'bhkpqvxz' # 0
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'bhkpqvxz'
posG = 'i'
posH = 'bhkpqvxz'
posI = 'g'
posJ = 'bhkpqvxz'
posK = 'bhkpqvxz'
posL = 'r'
posM = 'n'
posN = 'w'
posO = 't'
posP = 'bhkpqvxz' # 0
posQ = 'l'
posR = 'u'
posS = 'bhkpqvxz' # 0
posT = 'e'
posU = 'bhkpqvxz'
posV = 'y'
posW = 'j'
posX = 'a'
posY = 'm'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','i','g','r','n','w','t','l','u','e',
                         'y','j','a','m','c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # bhkpqvxz

# probando en jtbjqt     
for p in dic:
    if len(p) == 6:
        if (p[0] in posJ and p[1] in posT and p[2] in posB and p[3] in posJ
            and p[4] in posQ and p[5] in posT):
            c = c + 1
            print(p)
print(c)  
# 1 resultado: people
"""
"""
posA = 'bhkpqvxz' # 0
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'bhkpqvxz'
posG = 'i'
posH = 'bhkpqvxz'
posI = 'g'
posJ = 'p'
posK = 'bhkpqvxz'
posL = 'r'
posM = 'n'
posN = 'w'
posO = 't'
posP = 'bhkpqvxz' # 0
posQ = 'l'
posR = 'u'
posS = 'bhkpqvxz' # 0
posT = 'e'
posU = 'bhkpqvxz'
posV = 'y'
posW = 'j'
posX = 'a'
posY = 'm'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','i','g','p','r','n','w','t','l','u',
                         'e','y','j','a','m','c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # bhkqvxz

# probando en exlktco 
for p in dic:
    if len(p) == 7:
        if (p[0] in posE and p[1] in posX and p[2] in posL and p[3] in posK
            and p[4] in posT and p[5] in posC and p[6] in posO):
            c = c + 1
            print(p)
print(c)  
# 1 resultado: darkest
"""
"""
posA = 'bhqvxz' # 0
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'bhqvxz' # tentativa VZ -> tftlvoigmu | E_ERYTGIN_
posG = 'i'
posH = 'bhqvxz'
posI = 'h'
#tftlvoigmu | E_ERYTGIN_ (no concuerda con que i sea g
#asi que se revisa y se cometió un error en la primera combinacion, ya
#se corrige en esta parte)
posJ = 'p'
posK = 'k'
posL = 'r'
posM = 'n'
posN = 'w'
posO = 't'
posP = 'bhqvxz' # 0
posQ = 'l'
posR = 'u'
posS = 'bhqvxz' # 0
posT = 'e'
posU = 'bhqvxz'
posV = 'y'
posW = 'j'
posX = 'a'
posY = 'm'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','i','g','p','k','r','n','w','t','l',
                         'u','e','y','j','a','m','c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # bhqvxz

# probando en htigme  
for p in dic:
    if len(p) == 6:
        if (p[0] in posH and p[1] in posT and p[2] in posI and p[3] in posG
            and p[4] in posM and p[5] in posE):
            c = c + 1
            print(p)
print(c)  
# 1 resultado: behind
"""

posA = 'gqvxz' # 0
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'gqvxz'
posG = 'i'
posH = 'b'
posI = 'h'
posJ = 'p'
posK = 'k'
posL = 'r'
posM = 'n'
posN = 'w'
posO = 't'
posP = 'gqvxz' # 0
posQ = 'l'
posR = 'u'
posS = 'gqvxz' # 0
posT = 'e'
posU = 'gqvxz'
posV = 'y'
posW = 'j'
posX = 'a'
posY = 'm'
posZ = 'c'
c = 0

# funcion para definir nuesto nuevo alfabeto quitando los caracteres encontrados
nuevoAlfabeto = 'abcdefghijklmnopqrstuvwxyz'
caracteresEncontrados = ['o','s','f','d','i','b','h','p','k','r','n','w','t',
                         'l','u','e','y','j','a','m','c']
for a in caracteresEncontrados:
    nuevoAlfabeto = nuevoAlfabeto.replace(a, "")
print (nuevoAlfabeto) # gqvxz

# probando en ybfgmu  
for p in dic:
    if len(p) == 6:
        if (p[0] in posY and p[1] in posB and p[2] in posF and p[3] in posG
            and p[4] in posM and p[5] in posU):
            c = c + 1
            print(p)
print(c)
# 1 resultado: moving

posA = 'X' # 0
posB = 'o'
posC = 's'
posD = 'f'
posE = 'd'
posF = 'v'
posG = 'i'
posH = 'b'
posI = 'h'
posJ = 'p'
posK = 'k'
posL = 'r'
posM = 'n'
posN = 'w'
posO = 't'
posP = 'X' # 0
posQ = 'l'
posR = 'u'
posS = 'X' # 0
posT = 'e'
posU = 'g'
posV = 'y'
posW = 'j'
posX = 'a'
posY = 'm'
posZ = 'c'
c = 0

# Aqui termina el abecedario, asi que lo armamos y desciframos:

alfabetoFinal = "XosfdvibhpkrnwtXluXegyjamc"
print (descifraSustituye(cifrado,"XosfdvibhpkrnwtXluXegyjamc"))

