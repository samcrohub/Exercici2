#! /usr/bin/env python
# encoding: utf-8

print "per sortir de la aplicació escriu 'fi' quan et pregunti pel teu nom"
salir=0

while salir !="fi":
	"""declaramos aquí la variable para que el while nos vuelva a preguntar"""
	salir= raw_input ("Escriu el teu nom: ")
	"""ponemos una condición para que nos deje salir"""
	if salir == "fi":
		print "Adeu"
		break 
		"""ponemos aquí el break porque sino no nos dejaba salir"""
	numero= int (raw_input ("Escriu un numero: "))
	for i in range(numero):
		print salir,"\t","\t"
	if salir == "fi":
		print "Adeu"
	


