from django.db import models

# Create your models here.
class Bingo(models.Model):
    encabezado=models.CharField(max_length=100)
    organiza=models.TextField(null=True,blank=True)
    fecha=models.DateTimeField(null=True,blank=True)
    direccion=models.TextField(null=True,blank=True)
    valor=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    premios=models.TextField(null=True,blank=True)
    bolos=models.IntegerField(default=100)
    cantidad=models.IntegerField(default=0)

class Bolo(models.Model):
    bingos=models.ForeignKey(Bingo,on_delete=models.CASCADE,null=True, blank=True)
    b=models.IntegerField(default=0)
    i=models.IntegerField(default=0)
    n = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    o = models.IntegerField(default=0)
