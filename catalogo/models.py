from django.db import models
from django.utils import timezone

# Create your models here.
class machine(models.Model):
    nome_macchina = models.CharField(max_length = 400)
    tipo_macchina = models.CharField(max_length = 200)
    descrizione_macchina = models.TextField()
    data_creazione = models.DateTimeField(default = timezone.now)
    data_publicazione = models.DateTimeField(blank=True, null=True)
    # upload immagine da fare
    
    
    def publica(self):
        self.data_publicazione = timezone.now()
        self.save()
    def __str__(self):
        return self.nome_macchina


     
