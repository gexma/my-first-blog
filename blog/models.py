from django.db import models
from django.utils import timezone


class Post(models.Model):
    autore = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titolo = models.CharField(max_length=200)
    testo = models.TextField()
    data_creazione = models.DateTimeField(
            default=timezone.now)
    dat_pubblicazione = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.data_pubblicazione = timezone.now()
        self.save()

    def __str__(self):
        return self.titolo