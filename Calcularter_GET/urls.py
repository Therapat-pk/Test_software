
from django.urls import include,path
#from .views import *
#from Calcularter_GET import views
from Calcularter_GET import views

urlpatterns = [
    path("",views.index_GET,name="index_GET")
]