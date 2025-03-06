def cargaPalabras(): # cargamos diccionario
    archivo = open('italiano_diccionario.txt', 'r', encoding='utf-8')
    renglon = archivo.readline()
    palabras = renglon.split()
    print (len(palabras), 'palabras leidas')
    return palabras

def cargaCifrado(): # cargamos texto cifrado 1
    archivo = open('texto_2_cifrado.txt', 'r', encoding='utf-8')
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
posA = 'abcdefghijklmnopqrstuvwxyz'
posB = 'abcdefghijklmnopqrstuvwxyz'
posC = 'abcdefghijklmnopqrstuvwxyz'
posD = 'abcdefghijklmnopqrstuvwxyz'
posE = 'abcdefghijklmnopqrstuvwxyz'
posF = 'abcdefghijklmnopqrstuvwxyz'
posG = 'abcdefghijklmnopqrstuvwxyz'
posH = 'abcdefghijklmnopqrstuvwxyz'
posI = 'abcdefghijklmnopqrstuvwxyz' # 0
posJ = 'abcdefghijklmnopqrstuvwxyz'
posK = 'abcdefghijklmnopqrstuvwxyz'
posL = 'abcdefghijklmnopqrstuvwxyz'
posM = 'abcdefghijklmnopqrstuvwxyz'
posN = 'abcdefghijklmnopqrstuvwxyz'
posO = 'abcdefghijklmnopqrstuvwxyz'
posP = 'abcdefghijklmnopqrstuvwxyz'
posQ = 'abcdefghijklmnopqrstuvwxyz'
posR = 'abcdefghijklmnopqrstuvwxyz' # 0
posS = 'abcdefghijklmnopqrstuvwxyz' # 0
posT = 'abcdefghijklmnopqrstuvwxyz'
posU = 'abcdefghijklmnopqrstuvwxyz'
posV = 'abcdefghijklmnopqrstuvwxyz'
posW = 'abcdefghijklmnopqrstuvwxyz'
posX = 'abcdefghijklmnopqrstuvwxyz' # 0
posY = 'abcdefghijklmnopqrstuvwxyz' # 0
posZ = 'abcdefghijklmnopqrstuvwxyz'
c = 0

#probando con pzompwove    
for p in dic:
    if len(p) == 9:
        if (p[2] == p[6] and p[0] == p[4]
            and p[0] != p[1] and p[0] != p[2] and p[0] != p[3] and p[0] != p[5]
            and p[0] != p[6] and p[0] != p[7] and p[0] != p[8]
            and p[1] != p[2] and p[1] != p[3] and p[1] != p[4] and p[1] != p[5]
            and p[1] != p[6] and p[1] != p[7] and p[1] != p[8]
            and p[2] != p[3] and p[2] != p[4] and p[2] != p[5] and p[2] != p[7]
            and p[2] != p[8]
            and p[3] != p[4] and p[3] != p[5] and p[3] != p[6] and p[3] != p[7]
            and p[3] != p[8]
            and p[4] != p[5] and p[4] != p[6] and p[4] != p[7] and p[4] != p[8]
            and p[5] != p[6] and p[5] != p[7] and p[5] != p[8]
            and p[6] != p[7] and p[6] != p[8]
            and p[7] != p[8]):
            c = c + 1
            print(p)
print(c)
# 6 palabras
"""
"""
posA = 'abcdefghijklmnopqrstuvwxyz'
posB = 'abcdefghijklmnopqrstuvwxyz'
posC = 'abcdefghijklmnopqrstuvwxyz'
posD = 'abcdefghijklmnopqrstuvwxyz'
posE = 'oei'
posF = 'abcdefghijklmnopqrstuvwxyz'
posG = 'abcdefghijklmnopqrstuvwxyz'
posH = 'abcdefghijklmnopqrstuvwxyz'
posI = 'abcdefghijklmnopqrstuvwxyz' # 0
posJ = 'abcdefghijklmnopqrstuvwxyz'
posK = 'abcdefghijklmnopqrstuvwxyz'
posL = 'abcdefghijklmnopqrstuvwxyz'
posM = 'fgmu'
posN = 'abcdefghijklmnopqrstuvwxyz'
posO = 'ian'
posP = 'aeim'
posQ = 'abcdefghijklmnopqrstuvwxyz'
posR = 'abcdefghijklmnopqrstuvwxyz' # 0
posS = 'abcdefghijklmnopqrstuvwxyz' # 0
posT = 'abcdefghijklmnopqrstuvwxyz'
posU = 'abcdefghijklmnopqrstuvwxyz'
posV = 'ctr'
posW = 'trnde'
posX = 'abcdefghijklmnopqrstuvwxyz' # 0
posY = 'abcdefghijklmnopqrstuvwxyz' # 0
posZ = 'lsmno'
c = 0

#probando con ozo    
for p in dic:
    if len(p) == 3:
        if (p[0] == p[2] and p[0] in posO and p[1] in posZ):
            c = c + 1
            print(p)
print(c)
# 3 palabras | ala ama non
"""
"""
posA = 'abcdefghijklmnopqrstuvwxyz'
posB = 'abcdefghijklmnopqrstuvwxyz'
posC = 'abcdefghijklmnopqrstuvwxyz'
posD = 'abcdefghijklmnopqrstuvwxyz'
posE = 'oei'
posF = 'abcdefghijklmnopqrstuvwxyz'
posG = 'abcdefghijklmnopqrstuvwxyz'
posH = 'abcdefghijklmnopqrstuvwxyz'
posI = 'abcdefghijklmnopqrstuvwxyz' # 0
posJ = 'abcdefghijklmnopqrstuvwxyz'
posK = 'abcdefghijklmnopqrstuvwxyz'
posL = 'abcdefghijklmnopqrstuvwxyz'
posM = 'fgmu'
posN = 'abcdefghijklmnopqrstuvwxyz'
posO = 'an'
posP = 'aeim'
posQ = 'abcdefghijklmnopqrstuvwxyz'
posR = 'abcdefghijklmnopqrstuvwxyz' # 0
posS = 'abcdefghijklmnopqrstuvwxyz' # 0
posT = 'abcdefghijklmnopqrstuvwxyz'
posU = 'abcdefghijklmnopqrstuvwxyz'
posV = 'ctr'
posW = 'trnde'
posX = 'abcdefghijklmnopqrstuvwxyz' # 0
posY = 'abcdefghijklmnopqrstuvwxyz' # 0
posZ = 'lmo'
c = 0

#probando con lzoz    
for p in dic:
    if len(p) == 4:
        if (p[1] == p[3] and p[1] in posZ and p[2] in posO
            and p[0] != p[1] and p[0] != p[2]):
            c = c + 1
            print(p)
print(c)
# 4 palabras | cono dono imam sono
"""
"""
posA = 'abcdefghijklmnopqrstuvwxyz'
posB = 'abcdefghijklmnopqrstuvwxyz'
posC = 'abcdefghijklmnopqrstuvwxyz'
posD = 'abcdefghijklmnopqrstuvwxyz'
posE = 'oei'
posF = 'abcdefghijklmnopqrstuvwxyz'
posG = 'abcdefghijklmnopqrstuvwxyz'
posH = 'abcdefghijklmnopqrstuvwxyz'
posI = 'abcdefghijklmnopqrstuvwxyz' # 0
posJ = 'abcdefghijklmnopqrstuvwxyz'
posK = 'abcdefghijklmnopqrstuvwxyz'
posL = 'cdis'
posM = 'fgmu'
posN = 'abcdefghijklmnopqrstuvwxyz'
posO = 'an'
posP = 'aeim'
posQ = 'abcdefghijklmnopqrstuvwxyz'
posR = 'abcdefghijklmnopqrstuvwxyz' # 0
posS = 'abcdefghijklmnopqrstuvwxyz' # 0
posT = 'abcdefghijklmnopqrstuvwxyz'
posU = 'abcdefghijklmnopqrstuvwxyz'
posV = 'ctr'
posW = 'trnde'
posX = 'abcdefghijklmnopqrstuvwxyz' # 0
posY = 'abcdefghijklmnopqrstuvwxyz' # 0
posZ = 'mo'
c = 0

#probando con Vmvvd     
for p in dic:
    if len(p) == 5:
        if (p[0] == p[2] and p[0] == p[3] and p[0] in posV and p[1] in posM
            and p[1] != p[4]):
            c = c + 1
            print(p)
print(c)
# 5 palabras | cucce tutta tutte tutti tutto
"""
"""
posA = 'abcdefghijklmnopqrstuvwxyz'
posB = 'abcdefghijklmnopqrstuvwxyz'
posC = 'abcdefghijklmnopqrstuvwxyz'
posD = 'aeio'
posE = 'oei'
posF = 'abcdefghijklmnopqrstuvwxyz'
posG = 'abcdefghijklmnopqrstuvwxyz'
posH = 'abcdefghijklmnopqrstuvwxyz'
posI = 'abcdefghijklmnopqrstuvwxyz' # 0
posJ = 'abcdefghijklmnopqrstuvwxyz'
posK = 'abcdefghijklmnopqrstuvwxyz'
posL = 'cdis'
posM = 'u'
posN = 'abcdefghijklmnopqrstuvwxyz'
posO = 'an'
posP = 'aeim'
posQ = 'abcdefghijklmnopqrstuvwxyz'
posR = 'abcdefghijklmnopqrstuvwxyz' # 0
posS = 'abcdefghijklmnopqrstuvwxyz' # 0
posT = 'abcdefghijklmnopqrstuvwxyz'
posU = 'abcdefghijklmnopqrstuvwxyz'
posV = 'ct'
posW = 'trnde'
posX = 'abcdefghijklmnopqrstuvwxyz' # 0
posY = 'abcdefghijklmnopqrstuvwxyz' # 0
posZ = 'mo'
c = 0

#probando con mod     
for p in dic:
    if len(p) == 3:
        if (p[0] in posM and p[1] in posO and p[2] in posD
            and p[0] != p[1] and p[0] != p[2]
            and p[1] != p[2]):
            c = c + 1
            print(p)
print(c)
# 4 palabras | una une uni uno
"""
"""
posA = 'abcdefghijklmopqrstvwxyz'
posB = 'abcdefghijklmopqrstvwxyz'
posC = 'abcdefghijklmopqrstvwxyz'
posD = 'aeio'
posE = 'oei'
posF = 'abcdefghijklmopqrstvwxyz'
posG = 'abcdefghijklmopqrstvwxyz'
posH = 'abcdefghijklmopqrstvwxyz'
posI = 'abcdefghijklmopqrstvwxyz' # 0
posJ = 'abcdefghijklmopqrstvwxyz'
posK = 'abcdefghijklmopqrstvwxyz'
posL = 'cdis'
posM = 'u'
posN = 'abcdefghijklmopqrstvwxyz'
posO = 'n'
posP = 'aeim'
posQ = 'abcdefghijklmopqrstvwxyz'
posR = 'abcdefghijklmopqrstvwxyz' # 0
posS = 'abcdefghijklmopqrstvwxyz' # 0
posT = 'abcdefghijklmopqrstvwxyz'
posU = 'abcdefghijklmopqrstvwxyz'
posV = 'ct'
posW = 'trde'
posX = 'abcdefghijklmopqrstvwxyz' # 0
posY = 'abcdefghijklmopqrstvwxyz' # 0
posZ = 'mo'
c = 0

#probando con gwoqee     
for p in dic:
    if len(p) == 6:
        if (p[1] in posW and p[2] in posO and p[4] == p[5] and p[4] in posE):
            c = c + 1
            print(p)
print(c)
# 2 palabras | pendii vendee
"""
"""
posA = 'abcefghijklmopqrstvwxyz'
posB = 'abcefghijklmopqrstvwxyz'
posC = 'abcefghijklmopqrstvwxyz'
posD = 'aeio'
posE = 'ei'
posF = 'abcefghijklmopqrstvwxyz'
posG = 'pu'
posH = 'abcefghijklmopqrstvwxyz'
posI = 'abcefghijklmopqrstvwxyz' # 0
posJ = 'abcefghijklmopqrstvwxyz'
posK = 'abcefghijklmopqrstvwxyz'
posL = 'cis'
posM = 'u'
posN = 'abcefghijklmopqrstvwxyz'
posO = 'n'
posP = 'aeim'
posQ = 'd'
posR = 'abcefghijklmopqrstvwxyz' # 0
posS = 'abcefghijklmopqrstvwxyz' # 0
posT = 'abcefghijklmopqrstvwxyz'
posU = 'abcefghijklmopqrstvwxyz'
posV = 'ct'
posW = 'e'
posX = 'abcefghijklmopqrstvwxyz' # 0
posY = 'abcefghijklmopqrstvwxyz' # 0
posZ = 'mo'
c = 0

#probando con kegeqe     
for p in dic:
    if len(p) == 6:
        if (p[0] in posK and p[1] in posE and p[2] in posG and p[3] == p[1]
            and p[4] in posQ and p[5] == p[1]):
            c = c + 1
            print(p)
print(c)
# 1 palabra | lipidi
"""
"""
posA = 'abcefghjkmoqrstvwxyz'
posB = 'abcefghjkmoqrstvwxyz'
posC = 'abcefghjkmoqrstvwxyz'
posD = 'aeo'
posE = 'i'
posF = 'abcefghjkmoqrstvwxyz'
posG = 'p'
posH = 'abcefghjkmoqrstvwxyz'
posI = 'abcefghjkmoqrstvwxyz' # 0
posJ = 'abcefghjkmoqrstvwxyz'
posK = 'l'
posL = 'cs'
posM = 'u'
posN = 'abcefghjkmoqrstvwxyz'
posO = 'n'
posP = 'aem'
posQ = 'd'
posR = 'abcefghjkmoqrstvwxyz' 
posS = 'abcefghjkmoqrstvwxyz' # 0
posT = 'abcefghjkmoqrstvwxyz' # 0
posU = 'abcefghjkmoqrstvwxyz'
posV = 'ct'
posW = 'e'
posX = 'abcefghjkmoqrstvwxyz' # 0
posY = 'abcefghjkmoqrstvwxyz' # 0
posZ = 'mo'
c = 0

#probando con rdjvz      
for p in dic:
    if len(p) == 5:
        if (p[0] in posR and p[1] in posD and p[2] in posJ and p[3] in posV
            and p[4] in posZ
            and p[0] != p[1] and p[0] != p[2] and p[0] != p[3] and p[0] != p[4]
            and p[1] != p[2] and p[1] != p[3] and p[1] != p[4]
            and p[2] != p[3] and p[2] != p[4]
            and p[3] != p[4]):
            c = c + 1
            print(p)
print(c)
# 17 palabras
"""
"""
posA = 'abcefghjkmqrstvwxyz'
posB = 'abcefghjkmqrstvwxyz'
posC = 'abcefghjkmqrstvwxyz'
posD = 'ae'
posE = 'i'
posF = 'abcefghjkmqrstvwxyz'
posG = 'p'
posH = 'abcefghjkmqrstvwxyz'
posI = 'abcefghjkmqrstvwxyz' # 0
posJ = 'acrs'
posK = 'l'
posL = 'cs'
posM = 'u'
posN = 'abcefghjkmqrstvwxyz'
posO = 'n'
posP = 'aem'
posQ = 'd'
posR = 'bcfgmrsv' 
posS = 'abcefghjkmqrstvwxyz' # 0
posT = 'abcefghjkmqrstvwxyz' # 0
posU = 'abcefghjkmqrstvwxyz'
posV = 'ct'
posW = 'e'
posX = 'abcefghjkmqrstvwxyz' # 0
posY = 'abcefghjkmqrstvwxyz' # 0
posZ = 'o'
c = 0


#probando con rzllw      
for p in dic:
    if len(p) == 5:
        if (p[0] in posR and p[1] in posZ and p[2] in posL and p[3] == p[2]
            and p[4] in posW
            and p[0] != p[1] and p[0] != p[2] and p[0] != p[4]
            and p[1] != p[2] and p[1] != p[4]
            and p[2] != p[4]):
            c = c + 1
            print(p)
print(c)
# 6 palabras | bocce fosse gocce mosse rocce rosse
"""
"""
posA = 'abcefghjkmqrstvwxyz'
posB = 'abcefghjkmqrstvwxyz'
posC = 'abcefghjkmqrstvwxyz'
posD = 'ae'
posE = 'i'
posF = 'abcefghjkmqrstvwxyz'
posG = 'p'
posH = 'abcefghjkmqrstvwxyz'
posI = 'abcefghjkmqrstvwxyz' # 0
posJ = 'acrs'
posK = 'l'
posL = 'cs'
posM = 'u'
posN = 'abcefghjkmqrstvwxyz'
posO = 'n'
posP = 'aem'
posQ = 'd'
posR = 'bfgmr' 
posS = 'abcefghjkmqrstvwxyz' # 0
posT = 'abcefghjkmqrstvwxyz' # 0
posU = 'abcefghjkmqrstvwxyz'
posV = 'ct'
posW = 'e'
posX = 'abcefghjkmqrstvwxyz' # 0
posY = 'abcefghjkmqrstvwxyz' # 0
posZ = 'o'
c = 0

#probando con hdlvd      
for p in dic:
    if len(p) == 5:
        if (p[0] in posH and p[1] in posD and p[2] in posL and p[3] in posV
            and p[4] in posD
            and p[0] != p[1] and p[0] != p[2] and p[0] != p[3] and p[0] != p[4]
            and p[1] != p[2] and p[1] != p[3]
            and p[2] != p[3] and p[2] != p[4]
            and p[3] != p[4]):
            c = c + 1
            print(p)
print(c)
# 6 palabras | bocce fosse gocce mosse rocce rosse
"""
"""
posA = 'abcefghjkmqrtvwxyz'
posB = 'abcefghjkmqrtvwxyz'
posC = 'abcefghjkmqrtvwxyz'
posD = 'ae'
posE = 'i'
posF = 'abcefghjkmqrtvwxyz'
posG = 'p'
posH = 'bcfrtv'
posI = 'abcefghjkmqrtvwxyz' # 0
posJ = 'acr'
posK = 'l'
posL = 's'
posM = 'u'
posN = 'abcefghjkmqrtvwxyz'
posO = 'n'
posP = 'aem'
posQ = 'd'
posR = 'bfgmr' 
posS = 'abcefghjkmqrtvwxyz' # 0
posT = 'abcefghjkmqrtvwxyz' # 0
posU = 'abcefghjkmqrtvwxyz'
posV = 'ct'
posW = 'e'
posX = 'abcefghjkmqrtvwxyz' # 0
posY = 'abcefghjkmqrtvwxyz' # 0
posZ = 'o'
c = 0

#probando con naw      
for p in dic:
    if len(p) == 3:
        if (p[0] in posN and p[1] in posA and p[2] in posW
            and p[0] != p[1] and p[0] != p[2]
            and p[1] != p[2]):
            c = c + 1
            print(p)
print(c)
# 11 palabras
"""
"""
posA = 'ctvwyhr'
posB = 'abcefghjkmqrtvwxyz'
posC = 'abcefghjkmqrtvwxyz'
posD = 'ae'
posE = 'i'
posF = 'abcefghjkmqrtvwxyz'
posG = 'p'
posH = 'bcfrtv'
posI = 'abcefghjkmqrtvwxyz' # 0
posJ = 'acr'
posK = 'l'
posL = 's'
posM = 'u'
posN = 'abcrt'
posO = 'n'
posP = 'aem'
posQ = 'd'
posR = 'bfgmr' 
posS = 'abcefghjkmqrtvwxyz' # 0
posT = 'abcefghjkmqrtvwxyz' # 0
posU = 'abcefghjkmqrtvwxyz'
posV = 'ct'
posW = 'e'
posX = 'abcefghjkmqrtvwxyz' # 0
posY = 'abcefghjkmqrtvwxyz' # 0
posZ = 'o'
c = 0

#probando con pzompwove      
for p in dic:
    if len(p) == 9:
        if (p[0] in posP and p[1] in posZ and p[2] in posO and p[3] in posM
            and p[4] in posP and p[5] in posW and p[6] in posO and p[7] in posV
            and p[8] in posE):
            c = c + 1
            print(p)
print(c)
# 1 palabra | monumenti
"""
"""
posA = 'bcghjklqwxyz'
posB = 'bcghjklqwxyz'
posC = 'bcghjklqwxyz'
posD = 'a' #//////////
posE = 'i' #////////////
posF = 'bcghjklqwxyz'
posG = 'p' #//////////
posH = 'v' # Da_ _ elo | Davvelo ///////
posI = 'bcghjklqwxyz' # 0
posJ = 'c'
posK = 'r' # dppwvvwkw | ammettele -> ammettere #//////////
posL = 's' #//////////
posM = 'u' #//////////
posN = 'bcghjklqwxyz'
posO = 'n' #//////////
posP = 'm' #//////////
posQ = 'd' #//////////
posR = 'f' # rzllw  | _osse -> fosse #//////////
posS = 'bcghjklqwxyz' # 0
posT = 'bcghjklqwxyz' # 0
posU = 'bcghjklqwxyz'
posV = 't' #//////////////////
posW = 'e' #//////////
posX = 'bcghjklqwxyz' # 0
posY = 'bcghjklqwxyz' # 0
posZ = 'o' # /////////////////
c = 0

#probando con umeoqe      
for p in dic:
    if len(p) == 6:
        if (p[0] in posU and p[1] in posM and p[2] in posE and p[3] in posO
            and p[4] in posQ and p[5] in posE):
            c = c + 1
            print(p)
print(c)
# 1 palabra | quindi
"""
"""
posA = 'bcghjklqwxyz'
posB = 'z' # qelvdobd  | distan_a -> distanza #//////////
posC = 'bcghjklqwxyz'
posD = 'a'
posE = 'i'
posF = 'bcghjklqwxyz'
posG = 'p'
posH = 'v'
posI = 'bcghjklqwxyz' # 0
posJ = 'c'
posK = 'r'
posL = 's'
posM = 'u'
posN = 'bcghjklqwxyz' 
posO = 'n'
posP = 'm'
posQ = 'd'
posR = 'f'
posS = 'bcghjklqwxyz' # 0
posT = 'bcghjklqwxyz' # 0
posU = 'q'
posV = 't'
posW = 'e'
posX = 'bcghjklqwxyz' # 0
posY = 'bcghjklqwxyz' # 0
posZ = 'o'
c = 0

#probando con fdccew      
for p in dic:
    if len(p) == 6:
        if (p[0] in posF and p[1] in posD and p[2] in posC and p[3] in posC
            and p[4] in posE and p[5] in posW and p[2] == p[3]):
            c = c + 1
            print(p)
print(c)
# 1 palabra | gabbie
"""
"""
posA = 'bcghjklqwxyz'
posB = 'z'
posC = 'b'
posD = 'a'
posE = 'i'
posF = 'g'
posG = 'p'
posH = 'v'
posI = 'bcghjklqwxyz' # 0
posJ = 'c'
posK = 'r'
posL = 's'
posM = 'u'
posN = 'bcghjklqwxyz' 
posO = 'n'
posP = 'm'
posQ = 'd'
posR = 'f'
posS = 'bcghjklqwxyz' # 0
posT = 'bcghjklqwxyz' # 0
posU = 'q'
posV = 't'
posW = 'e'
posX = 'bcghjklqwxyz' # 0
posY = 'bcghjklqwxyz' # 0
posZ = 'o'
c = 0

#probando con nevvd    
for p in dic:
    if len(p) == 5:
        if (p[0] in posN and p[1] in posE and p[2] in posV and p[3] in posV
            and p[4] in posD):
            c = c + 1
            print(p)
print(c)
# 2 palabra | citta gitta | g ya esta usado, asi que c
"""
"""
posA = 'bcghjklqwxyz'
posB = 'z'
posC = 'b'
posD = 'a'
posE = 'i'
posF = 'g'
posG = 'p'
posH = 'v'
posI = 'bcghjklqwxyz' # 0
posJ = 'c'
posK = 'r'
posL = 's'
posM = 'u'
posN = 'c' 
posO = 'n'
posP = 'm'
posQ = 'd'
posR = 'f'
posS = 'bcghjklqwxyz' # 0
posT = 'bcghjklqwxyz' # 0
posU = 'q'
posV = 't'
posW = 'e'
posX = 'bcghjklqwxyz' # 0
posY = 'bcghjklqwxyz' # 0
posZ = 'o'
c = 0

#probando con naw      
for p in dic:
    if len(p) == 3:
        if (p[0] in posN and p[1] in posA and p[2] in posW
            and p[0] != p[1] and p[0] != p[2]
            and p[1] != p[2]):
            c = c + 1
            print(p)
print(c)
# 1 palabra | che
"""

posA = 'h'
posB = 'z'
posC = 'b'
posD = 'a'
posE = 'i'
posF = 'g'
posG = 'p'
posH = 'v'
posI = 'bcghjklqwxyz' # 0
posJ = 'l' # della 
posK = 'r'
posL = 's'
posM = 'u'
posN = 'c' 
posO = 'n'
posP = 'm'
posQ = 'd'
posR = 'f'
posS = 'bcghjklqwxyz' # 0
posT = 'bcghjklqwxyz' # 0
posU = 'q'
posV = 't'
posW = 'e'
posX = 'bcghjklqwxyz' # 0
posY = 'bcghjklqwxyz' # 0
posZ = 'o'
c = 0

# Aqui termina el abecedario, asi que lo armamos y desciframos:

alfabetoFinal = "hzbaigpvXlrsucnmdfXXqteXXo"
alfabetoFinal = "abcdefghijklmnopqrstuvwxyz"
print (cifrado)
print (descifraSustituye(cifrado,"hzbaigpvXlrsucnmdfXXqteXXo"))


