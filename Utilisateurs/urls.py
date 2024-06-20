from django.urls import path
from . import views
from .views import ProfileView  
from .views import Index, Inscription, Connexion, profil, Logout, delete_account, update_account, welcome_view

#from .views import inscription, CustomLoginView


app_name = "Utilisateurs"
urlpatterns = [
    path('', views.Index, name='index'),
    path('inscription/', views.Inscription, name='inscription'),
    path('connexion/', views.Connexion, name='connexion'),
    path('profil/<int:id>/', views.profil, name='profil'),
    path('logout/', views.Logout, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('update_account/', views.update_account, name='update_account'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('profile/', ProfileView.as_view(), name='profile'),

    #path('confirmation_envoyee/', views.confirmation_sent, name='confirmation_sent'),
    #path('confirmation/<str:token>/', views.confirm_account, name='confirm_account'),
]  
