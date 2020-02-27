from django.db import models

# Create your models here.
class Varible_to_Calcular(models.Model):
    x=models.IntegerField(null=True)
    y=models.IntegerField(null=True)
    Symbol=models.CharField(max_length=100, null=True)
    resuit=models.IntegerField(null=True)