from rest_framework import viewsets

from arbre_genealogique.models.membre import Membre
from arbre_genealogique.serializers.membre import MembreSerializer

class MembreViewSet(viewsets.ModelViewSet):
    queryset = Membre.objects.all()
    serializer_class = MembreSerializer
