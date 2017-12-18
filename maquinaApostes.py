#! /usr/bin/env python
# encoding: utf-8

import random
avancos = random.randrange(0,6)
guanys = 0

finestra1 = random.randrange(0,10)
finestra2 = random.randrange(0,10)
finestra3 = random.randrange(0,10)

print "per avançar la casella 1 pulsa el numero 1, per avançar la casella 2 pulsa el numero 2, per avançar la casella 3 pulsa el 3, pero no avançar més i sortir pulsa 0"

boton=1

while boton!=0 and avancos>0:
	
	print avancos
	
	print "%i,%i,%i" %(finestra1,finestra2,finestra3)
		
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
		
	boton= raw_input ("quina casella vols fer que avanci?")	
	
	if boton=='1':
		finestra1 = random.randrange(0,9)
	elif boton=='2':
		finestra2 = random.randrange(0,9)
	elif boton=='3':
		finestra3 = random.randrange(0,9)
	elif boton=='0':
		break
	else:
		print "No puedes avanzar con ese número!"
		
	avancos -= 1
		
	
print "Has guanyat un total de %i euros" %(guanys)
