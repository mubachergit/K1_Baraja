p = ('o', 'c', 'e', 'b')
c = ('A','2','3','4','5','6','7','S','C','R')

pf = ('D', 'P', 'T', 'C')
cf = ('A','2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K')


def crea_baraja(palos, cartas):
    
    baraja = []
    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return baraja

baraja1 = crea_baraja(p,c)
baraja2 = crea_baraja(pf, cf)
print(baraja1)
print(baraja2)
