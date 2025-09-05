from django.shortcuts import render
from django.http import HttpResponse
from .models import Membre

def index(request):
    context = {"arbre": "rien"}
    return render(request, "arbre_genealogique/index.html", context)

def details_membre(request, id_membre):
    membre = Membre.objects.filter(id=id_membre).first()
    context = {"details_membre": membre}
    return render(request, "arbre_genealogique/details_membre.html", context)