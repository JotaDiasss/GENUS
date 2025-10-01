from django.db import models

from django.utils import timezone
import datetime

class feedback(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    detalhes = models.TextField(null=False)
    data = models.DateTimeField("Postado em: ")
    user = models.CharField(max_length=200, null=False)
    estrelas = models.IntegerField(default=0, null=False) 

    def __str__(self):
        return f"{self.titulo} : [{self.detalhes}]"
    
    def strcompleta(self):
        return f"{self.titulo} feito por: {self.user} no dia {self.data}"
    
    def recente(self):
        return self.data >= timezone.now() - datetime.timedelta(days=1)
    
    def star(self):
        return f"{self.estrelas}"