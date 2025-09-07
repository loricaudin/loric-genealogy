from django.shortcuts import render
from .models import Membre

from django.template.defaulttags import register

@register.filter(name='split')
def split(value, key): 
 
    value.split("key")
    return value.split(key)

def index(request):
    context = {"arbre": "rien"}
    return render(request, "arbre_genealogique/index.html", context)

def details_membre(request, id_membre):
    membre = Membre.objects.filter(id=id_membre).first()
    context = {"details_membre": membre}
    return render(request, "arbre_genealogique/details_membre.html", context)

def modifier_membre(request, id_membre):
    membre = Membre.objects.filter(id=id_membre).first()
    context = {"details_membre": membre}
    return render(request, "arbre_genealogique/modifier_membre.html", context)