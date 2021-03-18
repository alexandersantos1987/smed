from django.db import models

# Create your models here.
class Formacao(models.Model):

    tematica = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    data = models.DateTimeField()
    carga = models.IntegerField(default=4)
    ativa = models.BooleanField(default=True)
    img_url = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    publico = models.CharField(max_length=255)
    presenca = models.CharField(max_length=255)

    class Meta():
        verbose_name_plural = "Formações"

    def __str__(self):
        return self.tematica