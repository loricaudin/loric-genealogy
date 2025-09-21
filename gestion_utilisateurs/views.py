from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from arbre_genealogique.models import Membre
from arbre_genealogique.context_processors import membre_connecte

PAGE_INSCRIPTION = "registration/signup.html"
PAGE_MON_COMPTE = "mon_compte/mon_compte.html"

def recuperer_membre(prenom, nom, date_naissance):
    membre = Membre.objects.filter(prenom=prenom, nom_famille=nom, date_naissance=date_naissance, user=None).first()
    if membre:
        return membre
    else:
        return None

def recuperer_membre_par_id(uuid_membre):
    membre = Membre.objects.filter(uuid=uuid_membre, user=None).first()
    if membre:
        return membre
    else:
        return None

def register(request):
    contexte = {
        "utilisateur": {},
        "membre": None,
        "erreur": None
    }
    if request.method == 'POST':

        if not request.POST["id_membre"]: # 1ère partie
            contexte["utilisateur"]["prenom"] = request.POST["prenom"]
            contexte["utilisateur"]["nom_famille"] = request.POST["nom"]
            contexte["utilisateur"]["date_naissance"] = request.POST["date_naissance"]

            contexte["membre"] = recuperer_membre(
                contexte["utilisateur"]["prenom"],
                contexte["utilisateur"]["nom_famille"],
                contexte["utilisateur"]["date_naissance"]
            )
            if not contexte["membre"]:
                contexte["erreur"] = "Désolé, nous n'avons pas trouvé votre profil dans l'arbre généalogique ou bien vous n'avez pas le droit de créer un nouveau compte. Vérifier que vos informations sont correctes. Si le problème persiste, veuillez contacter l'administrateur pour demander l'accès (email : loricaudin@yahoo.fr)"

        else: # 2ème partie
            contexte["membre"] = recuperer_membre_par_id(request.POST["id_membre"])
            if not contexte["membre"]:
                contexte["erreur"] = "Une erreur s'est produite, veuillez reprendre la procédure depuis le début"
            else:
                contexte["utilisateur"]["identifiant"] = request.POST["identifiant"]

                if request.POST["mot-de-passe"] == "" or contexte["utilisateur"]["identifiant"] == "":
                    contexte["erreur"] = "Veuillez rentrer tous les champs"
                elif request.POST["mot-de-passe"] != request.POST["mot-de-passe-confirmation"]:
                    contexte["erreur"] = "Les mots de passes ne sont pas les mêmes"
                else:
                    try:
                        utilisateur = User.objects.create_user(
                            contexte["utilisateur"]["identifiant"],
                            "email@example.com",
                            request.POST["mot-de-passe"]
                        )
                        utilisateur.save()

                        contexte["membre"].user = utilisateur
                        contexte["membre"].save()

                        return HttpResponseRedirect("/compte/login")

                    except Exception as e:
                        #contexte["erreur"] = "Erreur de création du compte. Si le problème persiste, contacter l'administrateur (email : loricaudin@yahoo.fr)."# +" Détails : " + str(e)
                        contexte["erreur"] = "L'utilisateur existe déjà"
                        contexte["utilisateur"]["identifiant"] = ""
        return render(request, PAGE_INSCRIPTION, contexte)
    else:
        return render(request, PAGE_INSCRIPTION, {})



def mon_compte(request):
    contexte = {
        "succes": [],
        "erreur": []
    }
    if request.method == 'POST':

        # Si le nom d'utilisateur a changé :
        user = request.user
        if request.FILES.get('username') and request.POST["username"] != user.username:
            try:
                user.username = request.POST["username"]
                user.save()
                contexte["succes"].append("Le nom d'utilisateur a été modifié avec succès")
            except Exception as e:
                contexte["erreur"].append("Echec de la modification du nom d'utilisateur")
        
        membre = membre_connecte(request)["membre_connecte"]

        if membre:
            # Si la photo de profil a changé :
            if request.FILES.get('photo'):
                try:
                    photo = request.FILES['photo']
                    if str(photo) == "suppression-image.png": # Astuce pour indiquer qu'on supprime la photo de profil
                        membre.photo = None
                    else:
                        membre.photo = photo
                    
                    membre.save()
                    contexte["succes"].append("La photo de profil a été modifiée avec succès")
                except Exception as e:
                    contexte["erreur"].append("Echec de la modification de la photo de profil")
    
    return render(request, PAGE_MON_COMPTE, contexte)
