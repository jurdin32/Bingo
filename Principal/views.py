import random

from django.shortcuts import render

# Create your views here.
def generardor(inicial,tope):
    L=list(range(inicial,tope+1))
    random.shuffle(L) #baraja la lista
    L=L[:5] #crea otra lista con los 10 primeros elementos
    L.sort(reverse=False) #ordena la lista L10
    return L

def index(request):

    contexto={
        "cartones":Carton(2)
    }
    return render(request,"index.html",contexto)


def Carton(cantidad):
    lista=[]
    for x in range(cantidad+1):
        l1 = generardor(1, 20)
        l2 = generardor(21, 40)
        l3 = generardor(41, 60)
        l4 = generardor(61, 80)
        l5 = generardor(81, 100)
        for i in range(5):
            l3[2]=0
            lista.append({"B":l1[i],"I":l2[i],"N":l3[i],"G":l4[i],"O":l5[i]})
    print("Tabla",x,lista,"Numeros:",len(lista))
    return lista


