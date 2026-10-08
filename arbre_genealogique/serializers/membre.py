from rest_framework import serializers

from arbre_genealogique.models.membre import Membre

class MembreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = '__all__'
