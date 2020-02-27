from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    for i in ['plus',"minus","multiply","divide","history","continue"]:
        if i in request.POST:
            Mark=i
    if request.method == 'POST' and Mark in request.POST:
        
        
        Varible=Varible_Forms(request.POST)
        if Varible.is_valid():
            History_dict={}
            x=Varible.cleaned_data.get("x")
            y=Varible.cleaned_data.get("y")
            if Mark=="plus":
                resuit=x+y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit,Symbol="+")
                Save_daa.save()
                #return render(request, 'index.html',{"form":Varible , 'resuit':resuit,"p":request.POST})   
            elif Mark=="minus":
                resuit=x-y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit,Symbol="-")
                Save_daa.save()
            elif Mark=="multiply":
                resuit=x*y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit,Symbol="x")
                Save_daa.save()
            elif Mark=="divide":
                resuit=x/y
                Save_daa=Varible_to_Calcular(x=x,y=y,resuit=resuit,Symbol="/")
                Save_daa.save()
            elif Mark=="continue" and resuit.is_valid():
                print(5)

            for i in Varible_to_Calcular.objects.all():
                History_dict[i]=[i.x,i.Symbol,i.y,i.resuit]
                #History_dict={i:[i.x,i.Symbol,i.y,i.resuit]}
            
            return render(request, 'index.html',{"form":Varible , 'resuit':resuit,"p":request.POST,'model':History_dict.values(),"num":0}) 
    #elif request.method == 'POST' and "plus" in request.POST:
    #if request.method == 'POST' and "plus" in request.POST:
    #if request.method == 'POST' and "plus" in request.POST:
    else:
        Varible=Varible_Forms()
    return render(request, 'index.html',{"form":Varible})   

def home(request):
    return render(request, 'home.html')   
def about(request):
    return render(request, 'about.html')   




        


