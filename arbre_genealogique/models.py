from django.db import models
from django.contrib.auth.models import User
import uuid

def image_upload_path(instance, filename):
    return f'photos/{instance.uuid}/{filename}'

class Membre(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    prenom = models.CharField(max_length=100)
    liste_prenoms = models.CharField(max_length=255, blank=True, null=True)

    nom_famille = models.CharField(max_length=100)

    genre = models.CharField(choices=[("H", "Homme"), ("F", "Femme")], max_length=1, blank=True, null=True)

    date_naissance = models.DateField(blank=True, null=True)
    date_mort = models.DateField(blank=True, null=True)

    numero_telephone = models.CharField(max_length=30, blank=True, null=True)
    adresse_mail = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)

    photo = models.ImageField(upload_to=image_upload_path, blank=True, null=True)

    pere = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='enfants_pere'
    )
    mere = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='enfants_mere'
    )

    couple = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='en_couple_avec'
    )

    divorce = models.ManyToManyField(
        to='self',
        blank=True
    )

    biographie = models.CharField(max_length=1024, blank=True, null=True)

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='utilisateur_associe'
    )

    def __str__(self):
        return self.prenom + " " + self.nom_famille

    def nom_famille_pere(self):
        pere = Membre.objects.filter(id=self.pere.id).first()
        if pere != None:
            return pere.nom_famille
        return ""
    
    def nom_famille_mere(self):
        mere = Membre.objects.filter(id=self.mere.id).first()
        if mere != None:
            return mere.nom_famille
        return ""
    
    def enfants(self):
        return Membre.objects.filter(models.Q(pere=self) | models.Q(mere=self))
    
    def initiales(self):
        return self.prenom[0] + self.nom_famille[0]