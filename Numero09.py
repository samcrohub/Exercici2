#encoding: utf-8

h = int(raw_input("Introdueix un numero enter més gran que cero:"))

if h <= 0:
	print "Has d'introduir un número més gran que cero"
	
else:
	for i in range(h):
		for j in range(i+1):
			print "*", 
		print
