class Movimiento:
    def __init__(self, identificador):
        self.identificador = identificador
        self.choice = ""

    def choose(self):
        self.choice = input("{identificador}, seleccione entre las opciones UY, MX, US, CO, BR, AR : ".format(
            identificador=self.identificador))
        print("{identificador} fue seleccionada  {choice}".format(identificador=self.identificador, choice=self.choice))

    def toNumericalChoice(self):
        switcher = {
            "UY": 0,
            "MX": 1,
            "US": 2,
            "CO": 3,
            "BR": 4,
            "AR": 5
        }
        return switcher[self.choice]


class ConversorMoneda:
    def __init__(self, p1, p2, p3):
        self.rules = [
            [1, 0.48, 0.026, 121.5, 0.14, 4.86],
            [2.09, 1, 0.053, 253.12, 0.28, 10.13],
            [39.2, 18.78, 1, 4750.88, 5.29, 190.19],
            [0.0082, 0.0039, 0.00021, 1, 0.0011, 0.04],
            [7.39, 3.55, 0.19, 898.48, 1, 39.95],
            [0.21, 0.099, 0.0053, 24.95, 0.028, 1]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("El factor de conversión de monedas es de {result}".format(result=self.getResultAsString(result)))

        conversion = float(p3) * result
        print("El resultado de la conversión es {conversion}".format(conversion=self.getResultAsString(conversion)))

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        return result


class Conversion:
    def __init__(self):
        self.endConversion = False
        self.Movimiento = Movimiento("Para la moneda de entrada")
        self.secondMovimiento = Movimiento("Para la moneda de salida")
        self.moneda = input("Ingrese la cantidad a convertir : ", )
        print("La cantidad ingresada fue " + str(self.moneda))
        if int(self.moneda) < 0:
            print("La cantidad introducida es negativa. Hasta luego!!")
            self.endConversion = True

    def start(self):
        while not self.endConversion:
            ConversorMoneda(self.Movimiento, self.secondMovimiento, self.moneda)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Quiere hacer otra operación s/n: ")
        if answer == 's':
            self.moneda = input("Ingrese la cantidad a convertir : ", )
            print("La cantidad ingresada fue " + str(self.moneda))
            if int(self.moneda) < 0:
                print("La cantidad introducida es negativa. Hasta luego!!")
                self.endConversion = True
            ConversorMoneda(self.Movimiento, self.secondMovimiento, self.moneda)
            self.checkEndCondition()
        else:
            print("Gracias por utilizar la aplicación. Hasta luego!!")
            self.endConversion = True


Conversion = Conversion()
Conversion.start()
