from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    for i in ['plus',"minus","multiply","divide"]:
        if i in request.POST:
            Mark=i
    if request.method == 'POST' and Mark in request.POST:
        
        
        Varible=Varible_Forms(request.POST)
        if Varible.is_valid():
            x=Varible.cleaned_data.get("x")
            y=Varible.cleaned_data.get("y")
            if Mark=="plus":
                resuit=x+y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit)
                Save_daa.save()
                return render(request, 'index.html',{"form":Varible , 'resuit':resuit,"p":request.POST})   
            elif Mark=="minus":
                resuit=x-y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit)
                Save_daa.save()
            elif Mark=="multiply":
                resuit=x*y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit)
                Save_daa.save()
            elif Mark=="divide":
                resuit=x/y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit)
                Save_daa.save()
    #elif request.method == 'POST' and "plus" in request.POST:
    #if request.method == 'POST' and "plus" in request.POST:
    #if request.method == 'POST' and "plus" in request.POST:
    else:
        Varible=Varible_Forms()
    return render(request, 'index.html',{"form":Varible})   



        


