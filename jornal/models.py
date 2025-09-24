from django.db import models
import datetime
from django.utils import timezone

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    resumo = models.TextField(null=False)
    detalhes = models.TextField(null=False)
    data = models.DateTimeField("Postado em: ")
    reporter = models.CharField(max_length=200, null=False)


    def __str__(self):
        return f"{self.titulo} : [{self.resumo}]"
    
    def strcompleta(self):
        return f"{self.titulo} feito por: {self.reporter} no dia {self.data}"
    
    def recente(self):
        return self.data >= timezone.now() - datetime.timedelta(days=1)
    
    def noticia(self):
        return f"{self.detalhes}"
    

class Comentarios(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto = models.TextField(null=False)
    likes = models.IntegerField(default=0)
    data = models.DateTimeField("Postado em: ")
    usuario = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f"[{self.noticia}] : {self.texto}"


# Create your models here.
