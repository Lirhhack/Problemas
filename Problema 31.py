'''Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.'''

Total = int(input('Ingrese la cantidad de dinero que tiene : '))
draw = int(input('Ingrese la cantidad de dinero que desea retirar : '))

class MyAccount:
    def __init__(self,balance, retiro):
        self.balance = balance
        self.retiro = retiro

    def change(self):
        if self.retiro > self.balance:
            print('U dont have enought cash')
        else:
            self.salida = self.balance - self.retiro
            self.balance -= self.retiro
            return self.salida
    def consultar_saldo(self):
        print('Tu saldo es {0}'.format(self.balance))

salida, monedas = 0, [0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50, 100, 200]

Cuenta = MyAccount(Total,draw)
salida = Cuenta.change()
Cuenta.consultar_saldo()
cantidad = 0 #Cantidad de veces que se usa una moneda, si es muy grande
#se usan muchas monedas de 200
for x in range(len(monedas)-1,-1,-1):  #Empezamos a contar desde la moneda mas grande (200)
    if salida == monedas[x]: #Si el vuelto alcanza en una sola moneda, paramos el programa
        cantidad = 1
        print('Has usado {0} de monedas de {1}'.format(cantidad, monedas[x])) #imprimmos
        break
    elif salida >= monedas[x]: #Si la salida es mayor que la moneda empezamos a usarla
        cantidad = salida//monedas[x] #el // significa una division entera
        # y con esta division busco saber cuantas monedas pueden usarse
        salida = salida % monedas[x] #Luego le sacamos el resto para hacer que el nuevo vuelto
        #sea menor y pase a ser usado por la siguiente moneda
        #Ejemplo 80 salida, moneda de 50
        # 80 % 50 = 30 (de resto), Entonces ese 30 se queda como nuevo vuelto
        print('Has usado {0} de monedas de {1}'.format(cantidad,monedas[x]))
