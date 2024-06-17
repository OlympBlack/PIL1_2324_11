from django.urls import path
from . import views


app_name = "Utilisateurs"
urlpatterns = [
    path('', views.Index, name='index'),
    path('inscription/', views.Inscription, name='inscription'),
    path('connexion/', views.Connexion, name='connexion'),
    path('profil/', views.Profil, name='profil'),
]