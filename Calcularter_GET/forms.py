from django.forms import ModelForm
from .models import *

class Varible_Forms(ModelForm):
   class Meta:
      model = Varible_to_Calcular
      fields = ["x","y"]