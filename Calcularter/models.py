from django.db import models

# Create your models here.
class Varible_to_Calcular(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()
    resuit=models.IntegerField()
