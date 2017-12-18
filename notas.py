#encoding: utf-8

mitjana = 0
notamasbaja = 0
suma = 0
finalitzar = "N"
contador = 0
i = 0
while finalitzar !="S":
	nota = float(raw_input("Introdueix la teva nota: "))
	nom = raw_input("Introdueix el teu nom: ")
	suma += nota
	#gestión nota más baja
	if contador == 0:
		notamasbaja = nota
	else:
		if notamasbaja>nota:
			notamasbaja = nota
	
	contador += 1
	finalitzar = raw_input ("desitja finalitzar? [S/N]: ")
#gestión de la media
mitjana = suma/contador
print "Adéu" 
print mitjana, notamasbaja



"""
if numero > 0:
	i = 1
	while i <= numero:
		producto = producto * i
		i += 1
	print producto
	 
		
else:  
              
	print "Introdueix un numero valid més gran que cero" """

