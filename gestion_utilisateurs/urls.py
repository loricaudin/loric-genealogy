from django.urls import path, include

from . import views

app_name = "compte"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
]

""" path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("changer-mdp/", views.changer_mdp, name="changer-mdp") """