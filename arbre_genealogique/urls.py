from django.urls import path

from . import views

app_name = "arbre_genealogique"
urlpatterns = [
    path("", views.index, name="index"),
    path("arbre/", views.arbre, name="arbre"),
    path("arbre/<int:id_membre>/", views.details_membre, name="details_membre"),
    path("arbre/<int:id_membre>/enregistrer", views.enregistrer_modification_membre, name="enregistrer_modification_membre")
]