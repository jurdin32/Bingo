import random

from django.shortcuts import render


from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse

# Create your views here.
from Principal.models import Bingo, Bolo


def render_to_pdf(template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("utf8")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="application/pdf")
    return None

def Carton(id):
    lista = []
    cartones= []
    bingo=Bingo.objects.get(id=id)
    for x in range(bingo.cantidad):
        lista = []
        l1 = generardor(1, 20)
        l2 = generardor(21, 40)
        l3 = generardor(41, 60)
        l4 = generardor(61, 80)
        l5 = generardor(81, 100)
        for i in range(5):
            l3[2] = 0
            Bolo(b=l1[i],i=l2[i],n=l3[i],g=l4[i],o=l5[i],bingos=bingo).save()
    return cartones


def generardor(inicial,tope):
    L=list(range(inicial,tope+1))
    random.shuffle(L) #baraja la lista
    L=L[:5] #crea otra lista con los 10 primeros elementos
    L.sort(reverse=False) #ordena la lista L10
    return L

def index(request):

    contexto={
        "generados":Bingo.objects.all(),
    }
    return render(request,"index.html",contexto)
    #return render_to_pdf("index.html",contexto)

def procesar(request,n):
    result= Carton(n)
    return HttpResponse(result)

def ver(request,n):
    bingo = Bingo.objects.get(id=n)
    contexto= {
        "bingo":bingo,
        "bolas":Bolo.objects.filter(bingos=bingo)
    }
    #return render(request,"tablas.html",contexto)
    return render_to_pdf("tablas.html",contexto)



