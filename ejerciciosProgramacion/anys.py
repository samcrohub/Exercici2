#encoding: utf-8

nom = raw_input("Introdueix el teu nom: ")
edat = int(raw_input("Introdueix la teva edat: "))
anny = int(raw_input("Introdueix l'any actual: "))
okey = True

if nom=='':
    print "No has introduit un nom!"
    okey = False

if edat<0 or anny<0:
    print "Edat o any son negatius!"
    okey = False

if edat>=anny:
    print "No es possible tenir mes anys que l'any actual!"
    okey = False

if okey == True:
    j = 0
    for i in range((anny-edat),anny):
        if j==0:
            print "El %d va neixer" %(i)
        else:
            print "El %d tenia %d anys" %(i,j)
        j += 1

print "Adeu %s!" %(nom)
        
