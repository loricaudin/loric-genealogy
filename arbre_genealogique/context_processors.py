from .models import Membre

def photo_membre(request):
    if request.user.is_authenticated:
        membre = Membre.objects.filter(user=request.user).first()
        if membre:
            return {'photo_membre': membre.photo.url if membre and membre.photo else None}
    return {'photo_membre': None}

def initiales_membre(request):
    if request.user.is_authenticated:
        membre = Membre.objects.filter(user=request.user).first()
        if membre:
            return {'initiales_membre': membre.prenom[0] + membre.nom_famille[0]}
    return {'initiales_membre': None}
