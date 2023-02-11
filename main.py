class Participant:
    def __init__(self, name, dinero):
        self.name = name
        self.choice = ""
        self.dinero = dinero
        self.choicedinero = ""

    def choose(self):
        self.choice = input("{name}, seleccione entre las opciones UY, MX, US, CO, BR, AR : ".format(name=self.name))
        print("{name} seleccionada fue {choice}".format(name=self.name, choice=self.choice))

    def choosecantidad(self):
        self.choicedinero= input("Indique la cantidad a convertir : ".format(name=self.dinero))
        print("La cantidad de dinero a convertir es {choicedinero}".format(choicedinero=self.dinero))

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


class GameRound:
    def __init__(self, p1, p2, c12):
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
        print("El factor de conversión de moneda es {result}".format(result=self.getResultAsString(result)))

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = str(result)
        return res


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant("La moneda de entrada")
        self.secondParticipant = Participant("La moneda de salida")

    def start(self):
        game_round = GameRound(self.participant, self.secondParticipant)


game = Game()
game.start()
