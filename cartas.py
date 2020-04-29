import random


palos = ('o', 'c', 'e', 'b')
cartas = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')

class Cartas():
    def __init__(self):

        self.baraja = []
        
        for palo in palos:
            for carta in cartas:
                naipe = carta + palo
                self.baraja.append(naipe)

    def mezclar(self):
        self.baraja_mezclada = []
        
        while len(self.baraja) != len(self.baraja_mezclada):
            n = random.randint(0, (len(self.baraja)-1))
            while self.baraja[n] in self.baraja_mezclada:
                n = random.randint(0, (len(self.baraja)-1))
            self.baraja_mezclada.append(self.baraja[n])
        self.baraja[:] = self.baraja_mezclada
        return self.baraja


    def repartir(self, players, cards):
        self.players = players
        self.cards = cards

        res = []
        for p in range(self.players):
            res.append([])

        for ic in range(self.cards):
            for ij in range(self.players):
                carta = self.baraja.pop(0)
                res[ij].append(carta)

        return res

    def invertir(b):
        for i in range (len(b)//2):
            alm = b[i]
            b[i] = b[-i-1]
            b[-i-1] = alm