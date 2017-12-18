#! /usr/bin/env python
# encoding: utf-8

print "per sortir de la aplicació escriu 'fi' quan et pregunti pel teu nom"
salir=0
while salir !="fi":
	
	salir= raw_input ("Escriu el teu nom: ")
	if salir == "fi":
		print "Adeu"
		break
	numero= int (raw_input ("Escriu un numero: "))
	for i in range(numero):
		print salir,"\t","\t"
	if salir == "fi":
		print "Adeu"
	


