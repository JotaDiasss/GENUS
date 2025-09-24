from django.db import models
from django.utils import datetime

class Journal(models.Model):    
    title = models.CharField(max_length=50)
    created_by = models.CharField(max_length=200)

class Entrada(models.Model):
    journal = models.ForeignKey(Journal)
    note = models.TextField()
    date = models.DateField()  

    def sequencia(journal):
        sequenciatotal = 0
        sequenciaatual = 0
        hoje = datetime.date.today()
        compareData = hoje + datetime.timedelta(1) # Tomorrow

        # Using list() here pulls all the entries from the DB at once
        # Gets all Entrada dates for this journal and whose dates are <= hoje
        Entrada_datas = list(Entrada.objects.values("data").filter(journal=journal, date__lte = hoje).order_by("-data"))

        for data in Entrada_datas:
            # Get the difference btw the dates
            delta = compareData - data

            if delta.days == 1: # Keep the streak going!
                sequenciaatual += 1
            elif delta.days == 0: # Don't bother increasing the day if there's multiple ones on the same day
                pass
            else: # Awwww...
                break # The current streak is done, exit the loop

            compareData = data

        if sequenciaatual > sequenciatotal:
            sequenciatotal = sequenciaatual

        return sequenciatotal