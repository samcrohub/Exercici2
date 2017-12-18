#! /usr/bin/env python
# encoding: utf-8
planta=0
fin="n"
while fin!="s":
	respuesta=raw_input ("Quin botó vols apretar: 2->puja2, 1->puja1, -1->baixa1 i -2->baixa2, s per sotir: ")
	if respuesta=="s":
		break
	boton=int (respuesta)
	if boton==1 and planta < 2:
		planta=planta+1
		print "Ha llegado a la planta", planta
		"""print "Quieres salir?"
		if pis=="x":	
			print "Las puertas estan abiertas " """
					
	if boton==2 and planta < 1:
		planta=planta+2
		print "Ha llegado a la planta", planta, """ "Quieres salir?" """
		""" if pis=="x":	
			print "Las puertas estan abiertas "	"""
				
	if boton==-1 and planta > 0:
		planta=planta-1
		print "Ha llegado a la planta", planta
		"""print "Quieres salir?"
		if pis=="x":	
			print "Las puertas estan abiertas "	"""	
			
	if boton==-2 and planta > 1:
		planta=planta-2		
		print "Ha llegado a la planta", planta
		"""print "Quieres salir?"
		if pis=="x":	
			print "Las puertas estan abiertas "	"""
		
	else: 
		print "Aquest pis no existeix"
		
	fin=raw_input ("Quieres salir? s/n")
	
print "Adeu"
	
"""if fin=="s"
		break"""



"""else:print "Adeu" """
"""elif planta==1:print "No exite el piso 3"elif planta==2:
		print "No exite el piso 4"
		
	if pis==1:
		planta=planta+1
	
	if pis==-1:
		planta=planta-1
		
	if pis==-2:
		planta=planta-2
	print "Estas en la planta",planta
	respuesta= (raw_input ("Quieres salir del ascensor? "))
	
	
	if respuesta=="no":
		print "Vuelve a picar" """
		 
