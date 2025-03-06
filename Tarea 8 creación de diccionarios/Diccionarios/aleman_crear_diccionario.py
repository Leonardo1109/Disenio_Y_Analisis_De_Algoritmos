# Alfabeto en aleman

def cargaCifrado():
    with open("aleman_palabras.txt", 'r', encoding='utf-8') as archivo:
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
[' ', '!', "'", ',', '-', '.', '0', '1', ':', ';', '?', 'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'z', '«', '»', 'ß', 'ä', 'ö', 'ü', '–']

En donde !',-.01:;?«»– no deberian formar parte del
diccionario, las demas son letras asi que nuestro conjunto de caracteres es el
siguente:
abcdefghijklmnopqrstuvwxz
los ultimos caracteres causan conflicto asi que los sustituimos:
ßäöü
"""

a = a.lower()
a = a.replace("ß", "s").replace("ä", "a").replace("ö", "o").replace("ü", "u")


caracteresEspeciales = ['!', "'", ',', '-', '.', '0', '1', ':', ';', '?',
                        '«', '»', '–']

for caracter in caracteresEspeciales:
    a = a.replace(caracter, "")
lista = []
mostrar_caracteres(a)

palabras = a.split() #hacemos dividimos por palabras
palabras_unicas = set(palabras) #asigna palabras unicas
diccionario = (sorted(palabras_unicas)) #ordenamos alfabeticamente
diccionario = sorted(diccionario, key=lambda x: (len(x), x)) #ordenamos por longitud
diccionario = ' '.join(diccionario)
with open('aleman_diccionario.txt', 'w', encoding = 'utf-8') as archivo:
    archivo.write(diccionario)

