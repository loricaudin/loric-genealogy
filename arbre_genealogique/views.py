from django.shortcuts import get_object_or_404, render
from .models import Membre

from django.template.defaulttags import register

@register.filter(name='split')
def split(value, key): 
 
    value.split("key")
    return value.split(key)

def index(request):
    return render(request, "arbre_genealogique/index.html", {})

def arbre(request):
    liste_membres = Membre.objects.order_by("id")
    context = {"liste_membres": liste_membres}
    return render(request, "arbre_genealogique/arbre.html", context)

def details_membre(request, id_membre):
    membre = get_object_or_404(Membre, pk=id_membre)
    context = {"details_membre": membre}
    return render(request, "arbre_genealogique/details_membre.html", context)

def enregistrer_modification_membre(request, id_membre):
    """ membre = get_object_or_404(Membre, pk=id_membre)
    print(membre) """
    print("ok")
    return HttpResponse("OK")
    return membre