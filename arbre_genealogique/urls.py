from django.urls import path

from . import views

app_name = "arbre_genealogique"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_membre>", views.details_membre, name="details_membre")
]