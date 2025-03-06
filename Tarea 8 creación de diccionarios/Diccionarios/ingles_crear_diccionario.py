# Alfabeto en ingles

def cargaCifrado():
    with open("ingles_palabras.txt", 'r', encoding='utf-8') as archivo:
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
[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Nuestro conjunto de caracteres es el siguente:
abcdefghijklmnopqrstuvwxyz
"""

a = a.lower()
a = a.replace("à", "a").replace("á", "a").replace("â", "a").replace("ã", "a")
a = a.replace("æ", "a").replace("ç", "c").replace("é", "e").replace("ê", "e")
a = a.replace("í", "i").replace("î", "i").replace("ó", "o").replace("ô", "o")
a = a.replace("õ", "o").replace("ú", "u").replace("œ", "o")

caracteresEspeciales = ['!', "'", '(', ')', ',', '-', '.', '/', '0', '1',
                        '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?',
                        '[', ']', '^', '_', 'ª', '«', '»', '¿', '→']

for caracter in caracteresEspeciales:
    a = a.replace(caracter, "")

palabras = a.split() #hacemos dividimos por palabras
palabras_unicas = set(palabras) #asigna palabras unicas
diccionario = (sorted(palabras_unicas)) #ordenamos alfabeticamente
diccionario = sorted(diccionario, key=lambda x: (len(x), x)) #ordenamos por longitud
diccionario = ' '.join(diccionario)
with open('ingles_diccionario.txt', 'w') as archivo:
    archivo.write(diccionario)

