#from random import *

#a=randint(-100,200)
#if a%2==0:
#    print("Juhuslik arv on",a)
#    print(a,"-paaris arv")
#if a>0:
#    print(a,"suurem kui 0")
#else:
#    print(a, "väiksem kui 0 või võrdne 0-ga")

##<0,100 ei soovi, 0-59-"2", 60-75-"3",76-90-"4" 91-100="5"
#if a<0 or a>100:
#    print("Viga tulemustega!")
#elif a>=0 and a<60:
#    print("Hinne 2")
#elif a>=60 and a<76:
#    print("Hinne 3")
#elif a>=76 and a<91:
#    print("Hinne 4")
#else:
#    print("Hinne 5")


from random import *

#nimi=input("Mis on sinu nimi?") #upper()-"JUKU", lower()-"juku", capitalize()-"Juku"
#if nimi=="Juku":
#   print("Lähme kinno")
#   vanus=int(input("Kui vana sa oled?"))
#   if vanus<0 or vanus>120:
#       vastus="Viga vanusega"
#   elif vanus<6:
#         vastus="tasuta pilet"
#   elif vanus<14:
#         vastus="lastepilet"
#   elif vanus<65:
#         vastus="täispilet"
#   elif vanus<=120:
#         vastus="sooduspilet"
#   print("On vaja Jukule osta",vastus)
#else:
#    print("Joonistame")

#n1=input("Esimene nimi")
#n2=input("Teine nimi")
#if n1.upper()=="KARINA" and n2.upper()=="ERIK" or n1.upper()=="ERIK" and n2.upper()=="KARINA":
#    print("Pinginaabrid")
#else:
#    print("Nad ei ole naabrid")
#if n1.upper() in ["A","B"] and n2.upper() in ["A","B"]:
#    print("Pinginaabrid")
#else:
#    print("Nad ei ole naabrid")

#from random import *
##3
#pikkus=float(input("Põranda pikkus: "))
#laius=float(input("Põrand laius: "))
#pindala=pikkus*laius
#print("Toa põranda pindala on:",pindala)
#valik=input("Kas tahad remondi teha? ")
#if valik.lower()=="jah":
#    hind=float(input("Kui palju maksab ruutmeeter? "))
#    summa=hind*pindala
#    print("Põranda vahetamise summa on", summa)

#4
alghind=randint(0,1000000)/100 #0.00 - 1000.00
if alghind>700:
    soodustus=alghind*0.3
    alghind-=soodustus
    alghind*=0.7
print("Uus hind on ", alghind)
