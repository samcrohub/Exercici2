#! /usr/bin/env python
# encoding: utf-8

quantitat = int (raw_input ("introdueix una qunatitat de diners: "))

b500=0
b200=0
b100=0
b50=0
b20=0
b10=0
b5=0
m2=0
m1=0

while quantitat !=0: 
	if quantitat>=500:
		 quantitat -= 500
		 b500 += 1
		 
	elif quantitat>=200:
		 quantitat -= 200
		 b200 += 1
	elif quantitat>=100:
		 quantitat -= 100
		 b100 += 1
	elif quantitat>=50:
		 quantitat -= 50
		 b50 += 1
	elif quantitat>=20:
		 quantitat -= 20
		 b20 += 1
	elif quantitat>=10:
		 quantitat -= 10
		 b10 += 1
	elif quantitat>=2:
		 quantitat -= 2
		 m2 += 1
	elif quantitat>=1:
		 quantitat -= 1
		 m1 += 1



if b500>0:
	print "billetes de" b500
if b200>0:
	print "billetes de" b200
if b100>0:
	print "billetes de" b100
if b50>0:
	print "billetes de" b50
if b20>0:
	print "billetes de" b20
if b10>0:
	print "billetes de" b10
if b5>0:
	print "billetes de" b5
if m2>0:
	print "billetes de" m2
if m1>0:
	print "billetes de" m1
else:
	print "No tenemos cambio"

		
