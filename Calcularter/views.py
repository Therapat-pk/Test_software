from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        Varible=Varible_Forms(request.POST)
        if Varible.is_valid():
            x=Varible.cleaned_data.get("x")
            y=Varible.cleaned_data.get("y")
            resuit=x+y
            #Varible_to_Calcular.resuit=resuit
            #Varible.save()
            return render(request, 'index.html',{"form":Varible , 'resuit':resuit})   
    else:
        Varible=Varible_Forms()
    return render(request, 'index.html',{"form":Varible})   



        


