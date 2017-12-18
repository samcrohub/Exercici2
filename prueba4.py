#encoding: utf-8

import random

def comprova_coincidencia(finestra1,finestra2,finestra3,guanys):
    if finestra1==finestra2 and finestra2==finestra3:
        print "has guanyat 250€"
        guanys += 250
        finestra1 = random.randrange(0,9)
        finestra2 = random.randrange(0,9)
        finestra3 = random.randrange(0,9)
    elif finestra1==finestra2:
        print "has guanyat 20€"
        guanys += 20
        finestra1 = random.randrange(0,9)
        finestra2 = random.randrange(0,9)
    elif finestra2==finestra3:
        print "has guanyat 20€"
        guanys += 20
        finestra2 = random.randrange(0,9)
        finestra3 = random.randrange(0,9)
    elif finestra1==7 and finestra3==7:
        print "has guanyat 2€"
        guanys += 2
        finestra1 = random.randrange(0,9)
        finestra3 = random.randrange(0,9)
    elif finestra1==7:
        print "has guanyat 1€"
        guanys += 1
        finestra1 = random.randrange(0,9)
    elif finestra3==7:
        print "has guanyat 1€"
        guanys += 1
        finestra3 = random.randrange(0,9)
    else:
        print "no has guanyar res!"

    return finestra1,finestra2,finestra3,guanys

avancos = random.randrange(0,6)
guanys = 0

finestra1 = random.randrange(0,10)
finestra2 = random.randrange(0,10)
finestra3 = random.randrange(0,10)

while avancos>=0:

    print avancos

    print "%i\t%i\t%i" %(finestra1,finestra2,finestra3)
    
    # comprovacion de coincidencias
    finestra1,finestra2,finestra3,guanys = comprova_coincidencia(finestra1,finestra2,finestra3,guanys)
    

    boton = raw_input("Que ventana quieres actualizar: ") # 1, 2 o 3

    # comprovar que ventana mover
    if boton=='1':
        finestra1 = random.randrange(0,9)
    elif boton=='2':
        finestra2 = random.randrange(0,9)
    elif boton=='3':
        finestra3 = random.randrange(0,9)
    elif boton=='0':
        break
    else:
        print "te has equivocado!"

    avancos -= 1

print "Has guanyat un total de %i euros" %(guanys)
    
