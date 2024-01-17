#1

k=0
mitu=0
while k<15:
    k+=1
    n=float(input("Sisesta arv nr."+str(k)))
    if int(n)==float(n):
        mitu+=1
print("2.variant")
k=0
mitu=0
while True:
    k+=1
    n=float(input("Sisesta arv nr."+str(k)))
    if int(n)==float(n):
        mitu+=1
    if k==15: break
print("3.variant")
















k=0
mitu=0
while True:
    k+=1
    n=float(input("Sisesta arv nr."+str(k)))
    if int(n)==float(n):
        mitu+=1
    if k==15: break












mitu=0
for k in range(1,16):
    n=float(input("Sisesta arv nr. " +str(k)))
    if int(n)==float(n):
        mitu+=1
print("Täisarvude kogus: ",mitu)