import random  # Importamos la libreria random


def generar_cumpleaños():  # creamos una funcion que genera un cumpleaños
    mes = random.randint(1, 12)  # Agarra un mes cualquiera
    dia = random.randint(1, 31)  # Agarra un dia cualquiera
    return dia, mes  # retorna el dia y el mes


n = int(input('Ingrese la cantidad de personas que desea probar : '))
# la linea de arriba indica la cantidad de cumpleaños que crearemos o
# mejor dicho, la cantidad de personas que habran en la sala
List = []  # creamos una lista vacia
for x in range(0, n):  # hacemos un for desde 0 hasta la cantidad ingresada
    List.append(generar_cumpleaños())  # Agregamos cada cumpleaños generado
    #  a la lista
print(List)  # Imprimos la lista para ver que paso


if len(List) != len(list((set(List)))):
    print('Hay dos cumpleaños , felicidades')
else:
    print('No hay cumpleaños iguales ')
