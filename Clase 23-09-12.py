#                                   ARCHIVOS

archivo = open('prueba.txt', 'w')
# w = crea o sobreescribe y despues abre
# wb lo mismo pero binario
# r abre para lectura; marca error si no existe
# rb abre para lectura binario
# a abre para añadir

'''
archivo.write('linea 1') #no existe salto de linea, hy que ponerlo manual
archivo.write('linea 2')
archivo.write('linea 3')

archivo.write('\n\npalabra 1\n\npalabra2')
archivo.close()
'''

'''
archivo.write('Emiliano\nIvan\nDaniel\nRafael\nEmilio\nAlan\nDana')
archivo.close()

archivo = open('prueba.txt', 'r')
for renglon in archivo:
    print(renglon)
archivo.close()
'''
#                           CREANDO UN DICCIONARIO
a = "esta es una cadena de prueba para un ejercicio en clase"\
    " y queremos crear un pequeño diccionario para una tarea"\
    " donde vamos a quitar palabras repetidas querido diario"\
    " hoy el transporte estuvo insoportable me llevó un para"\
    " esta es te dedico una rosa en la cola porque te quiero"\
    " 1 2 5 8 9 11 25 1024185"
archivo.write(a)
archivo.close()

palabras=[]
archivo = open('prueba.txt', 'r') #'r', encording) pra no tener problemas con á,é, etc
for renglon in archivo:
    # renglon = renglon.lower() # para pasar el renglon  minusculas
    datos = renglon.split()
    for d in datos:
        if not (d) in palabras:
            palabras.append(d)
archivo.close()
print(palabras,"\n\n\n")
palabras.sort()
print(palabras)




