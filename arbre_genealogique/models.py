from django.db import models

class Membre(models.Model):

    prenom = models.CharField(max_length=100)
    liste_prenoms = models.CharField(max_length=255, blank=True, null=True)

    nom_famille = models.CharField(max_length=100)
    nom_famille_pere = models.CharField(max_length=100, blank=True, null=True)
    nom_famille_mere = models.CharField(max_length=100, blank=True, null=True)

    genre = models.CharField(choices=[("H", "Homme"), ("F", "Femme")], max_length=1)

    date_naissance = models.DateField(blank=True, null=True)
    date_mort = models.DateField(blank=True, null=True)

    numero_telephone = models.CharField(max_length=30, blank=True, null=True)
    adresse_mail = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)

    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    pere = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='enfants_pere'
    )
    mere = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='enfants_mere'
    )

    couple = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='en_couple_avec'
    )

    def __str__(self):
        return self.prenom + " " + self.nom_famille
    
    def enfants(self):
        return Membre.objects.filter(models.Q(pere=self) | models.Q(mere=self))