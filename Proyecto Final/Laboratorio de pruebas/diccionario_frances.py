# Alfabeto en frances

def cargaCifrado():
    with open("frances.txt", 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

a = cargaCifrado()

# funcion que mostrará los caracteres de nuestro texto
lista = []
def mostrar_caracteres(texto):
    texto = texto.lower()
    for c in texto:
        if c not in lista:
            lista.append(c)
    lista.sort()
    print (lista)
mostrar_caracteres(a)
"""
Los caracteres que se han encontrado son los siguentes:
[' ', '!', '%', '&', "'", '(', ')', '+', ',', '-', '.', '/', '0', '1', '2', '3',
'4', '5', '6', '7', '8', '9', ':', '>', '?', '[', ']', 'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z', '«', '°', '»', 'à', 'â', 'ç', 'è', 'é', 'ê', 'ë', 'í',
'î', 'ï', 'ó', 'ô', 'ù', 'û', 'œ', 'ᵉ', '–', '’', '…']
En donde !%&'()+,-./0123456789:>?[]«°»ᵉ–’… no deberian formar parte del
diccionario, las demas son letras asi que nuestro conjunto de caracteres es el
siguente:
abcdefghijklmnopqrstuvwxyz
los ultimos caracteres causan conflicto asi que los sustituimos:
àâçèéêëíîïóôùûœ
"""
a = a.lower()
a = a.replace("à", "a").replace("â", "a").replace("ç", "c").replace("è", "e")
a = a.replace("é", "e").replace("ê", "e").replace("ë", "e").replace("í", "i")
a = a.replace("î", "i").replace("ï", "i").replace("ó", "o").replace("ô", "o")
a = a.replace("ù", "u").replace("û", "u").replace("œ", "o")

caracteresEspeciales = ['!', '%', '&', "'", '(', ')', '+', ',', '-', '.',
                        '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        ':', '>', '?', '[', ']', '«', '°', '»', 'ᵉ', '–', '’',
                        '…']
for caracter in caracteresEspeciales:
    a = a.replace(caracter, "")

palabras = a.lower().split() #hacemos minusculas y dividimos por palabras
palabras_unicas = set(palabras) #asigna palabras unicas
diccionario = (sorted(palabras_unicas)) #ordenamos alfabeticamente
diccionario = sorted(diccionario, key=lambda x: (len(x), x)) #ordenamos por longitud
diccionario = ' '.join(diccionario)
with open('diccionarioFrances.txt', 'w') as archivo:
    archivo.write(diccionario)

