import random

def get_ganador(usuario, compu):
    if(usuario == 0 and compu == 2):
        return('usuario')
    if(usuario > compu):
        return('usuario')
    if(usuario == 2 and compu == 0):
        return('compu')
    if (compu > usuario):
        return('compu')
    else:
        return('empate')

def get_ganador2(usuario, compu):
    numero = (usuario - compu)%5
    if numero == 0:
        return('empate')
    elif (numero == 1 or numero == 2):
        return ('usuario')
    else:
        return ('compu') 

opciones = {0:'piedra', 1:'spock', 2:'papel', 3:'lagarto', 4:'tijeras'}
#El usuario da su opcion
print('0:piedra')
print('1:spock')
print('2:papel')
print('3:lagarto')
print('4:tijeras')
usuario = int(input('Escriba su opcion: '))
print(usuario)
compu = random.choice([0,1,2,3,4])
print('Usteded seleccionó: ',opciones[usuario])
print('La compu seleccionó: ', opciones[compu])

gana = get_ganador2(usuario, compu)
print('Y el ganador es: ', gana)


"""import random
   
def get_ganador2(usuario, compu):
    if (usuario - compu) == 0:
        return 'empate'
    elif ((usuario - compu)%5) == 1 or (usuario - compu)%5 == 2:
        return 'usuario'
    else:
        return 'compu'
        
opciones = {0:'piedra',1:'Spock',2:'papel',3:'lagarto',4:'tijeras'}
# el usuario da su opción
print('0:piedra')
print('1:Spock')
print('2:papel')
print('3:lagarto')
print('4:tijeras')
usuario = int(input('escriba su opción:'))
# la computadora escoje
compu = random.choice([0,1,2,3,4])
print('usted seleccionó: ',opciones[usuario])
print('la compu seleccionó: ',opciones[compu])
gana = get_ganador2(usuario, compu)
print('y el ganador es:', gana)
"""
