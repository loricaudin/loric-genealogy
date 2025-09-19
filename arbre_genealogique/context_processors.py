from .models import Membre

def membre_connecte(request):
    if request.user.is_authenticated:
        membre = Membre.objects.filter(user=request.user).first()
        if membre:
            return {'membre_connecte': membre}
    return {'membre_connecte': None}

