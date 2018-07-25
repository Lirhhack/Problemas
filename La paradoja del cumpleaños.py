import random 

def generar_cumpleaños(): 
    mes = random.randint(1, 12)  
    dia = random.randint(1, 31)  
    return dia, mes 

n = int(input('Ingrese la cantidad de personas que desea probar : '))
List = []  
for x in range(0, n):  
    List.append(generar_cumpleaños())  
    
if len(List) != len(list((set(List)))):
    print('Hay dos cumpleaños , felicidades')
else:
    print('No hay cumpleaños iguales ')
