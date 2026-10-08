from django.urls import path, include
from rest_framework.routers import DefaultRouter

from arbre_genealogique.views.api.membres import MembreViewSet

from .views import arbre_genealogique

api_router = DefaultRouter()
api_router.register('membres', MembreViewSet, basename="membre")

app_name = "arbre_genealogique"
urlpatterns = [
    path("", arbre_genealogique.index, name="index"),
    path('api/', include(api_router.urls)),
    path("arbre/", arbre_genealogique.arbre, name="arbre"),
    path("liste/", arbre_genealogique.liste, name="liste"),
    path("details/<int:id_membre>/", arbre_genealogique.details_membre, name="details_membre"),
    path("details/<int:id_membre>/enregistrer", arbre_genealogique.enregistrer_modification_membre, name="enregistrer_modification_membre")
]