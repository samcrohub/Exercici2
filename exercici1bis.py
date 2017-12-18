#! /usr/bin/env python
# encoding: utf-8

print "Preu Producte"
a= int(raw_input("Preu:"))
b= float(raw_input("IVA:"))
b=a*(b/100)
c=a+b
print "Preu de IVA:",b, "Preu amb IVA:",c

