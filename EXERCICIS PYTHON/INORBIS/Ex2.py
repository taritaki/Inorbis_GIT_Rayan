

def suma100primersnums():

    suma = 0
    for i in range(1, 101):  
        suma += i 
    return suma


def Corrector():
    resultat=suma100primersnums()
    if(resultat==5050):
        print("TEST OK")
    else:
        print("TEST NOT OK")


Corrector()
