from django.forms import ModelForm
from .models import *

class Varible_Forms(ModelForm):
   class Meta:
      model = Lecture
      fields = ["x","y"]