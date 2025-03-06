# Alfabeto en italiano

def cargaCifrado():
    with open("italiano_palabras.txt", 'r', encoding='utf-8') as archivo:
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
['\n', ' ', '!', '"', '%', "'", '(', ')', '+', ',', '-', '.', '/', '0', '1',
'2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?', '[', ']', '_', 'a', 'b',
'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '«', '»', 'à', 'á', 'â', 'è', 'é', 'ê',
'ë', 'ì', 'í', 'î', 'ï', 'ò', 'ó', 'ô', 'ù', 'ú', 'û', 'ü', '–', '—', '’', '“',
'”', '€']

En donde \n !"%'()+,-./0123456789:;?[]_«»–—’“”€ no deberian formar parte del
diccionario, las demas son letras asi que nuestro conjunto de caracteres es el
siguente:
abcdefghijklmnopqrstuvwxyz
los ultimos caracteres causan conflicto asi que los sustituimos:
àáâèéêëìíîïòóôùúûü

"""

a = a.lower()
a = a.replace("à", "a").replace("á", "a").replace("â", "a").replace("è", "e")
a = a.replace("é", "e").replace("ê", "e").replace("ë", "e").replace("ì", "i")
a = a.replace("í", "i").replace("î", "i").replace("ï", "i").replace("ò", "o")
a = a.replace("ó", "o").replace("ô", "o").replace("ù", "u").replace("ú", "u")
a = a.replace("û", "u").replace("ü", "u")

caracteresEspeciales = ['\n', '!', '"', '%', "'", '(', ')', '+', ',', '-',
                        '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                        '9', ':', ';', '?', '[', ']', '_', '«', '»', '–', '—',
                        '’', '“', '”', '€']
for caracter in caracteresEspeciales:
    a = a.replace(caracter, "")

palabras = a.split() #hacemos dividimos por palabras
palabras_unicas = set(palabras) #asigna palabras unicas
diccionario = (sorted(palabras_unicas)) #ordenamos alfabeticamente
diccionario = sorted(diccionario, key=lambda x: (len(x), x)) #ordenamos por longitud
diccionario = ' '.join(diccionario)
with open('italiano_diccionario.txt', 'w') as archivo:
    archivo.write(diccionario)
