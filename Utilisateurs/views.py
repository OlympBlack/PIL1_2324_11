from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from commondatab.models import ZzUsers
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import json
from django.core.exceptions import ValidationError
from datetime import datetime
from django.urls import reverse
"""from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

import os
from dotenv import load_dotenv

load_dotenv()"""

def Index(request):
    return render(request, "Utilisateurs/index.html")


# la fonction pour la page inscription
def Inscription(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password', '')
        sexe = request.POST.get('sexe', '')
        profile_media = request.FILES.get('profile_media')

        # Vérifier si le pseudo est présent
        if not pseudo:
            messages.error(request, 'Le pseudo est requis')
            return render(request, 'Utilisateurs/inscription.html')

        # Vérifier si l'email existe déjà
        if ZzUsers.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà")
            return render(request, 'Utilisateurs/inscription.html')

        # Créer l'utilisateur
        user = ZzUsers.objects.create(
            email=email,
            pseudo=pseudo,
            password=make_password(password1),
            sex=sexe,
            profile_media=profile_media,
        )
        user.save()
        
        # Rediriger vers la page d'accueil après l'inscription
        return redirect(reverse('Utilisateurs:profil', kwargs={'id': user.id}))

    # Afficher le formulaire d'inscription
    return render(request, 'Utilisateurs/inscription.html') 


#fonction de connexion
def Connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('acceuil') 
        else:
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')
            return render(request, 'Utilisateurs/connexion.html')
    
    return render(request, 'Utilisateurs/connexion.html')


#fonction de la page profil
@login_required
def profil(request, id):
    user = get_object_or_404(ZzUsers, id=id)
    context = {'user': user}
    return render(request, 'Utilisateurs/profil.html', context)


#fonction de deconnection
@login_required
def Logout(request):
    logout(request)
    return redirect('Utilisateurs:connexion')


#la fonction pour supprimer son compte
@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Votre compte a été supprimé avec succès.')
        logout(request)
        return redirect('Utilisateurs:index') 


# la fonction pour la mise à jour du profil utilisateurs
@login_required
def update_account(request):
    if request.method == 'POST':
        user = request.user

        # Récupérer les données du formulaire avec des valeurs par défaut
        email = request.POST.get('email', 'aucun')
        pseudo = request.POST.get('pseudo', 'aucun')
        nom = request.POST.get('nom', 'aucun')
        prenom = request.POST.get('prenom', 'aucun')
        password = request.POST.get('password', 'aucun')  # Corrected typo
        birthday_str = request.POST.get('birthday', None)

        if birthday_str:
            try:
                birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
            except ValueError:
                birthday = None
        else:
            birthday = None

        bio = request.POST.get('bio', 'aucun')
        sex = request.POST.get('sex', 'aucun')
        plage = request.POST.get('plage', 'aucun')
        astre = request.POST.get('astre', 'aucun')
        religion = request.POST.get('religion', 'aucun')
        city = request.POST.get('city', 'aucun')
        country = request.POST.get('country', 'aucun')
        # hobby = request.POST.get('hobby', '[]')  
        # pref = request.POST.get('pref', '[]')  # JSON string

        # Mise à jour des champs de l'utilisateur
        user.email = email
        user.pseudo = pseudo
        user.nom = nom
        user.prenom = prenom
        user.password = password
        user.birthday = birthday
        user.bio = bio
        user.sex = sex
        user.plage = plage
        user.astre = astre
        user.religion = religion
        user.city = city
        user.country = country
        # user.hobby = json.loads(hobby)  # Convertir JSON string en Python list
        # user.pref = json.loads(pref)  # Convertir JSON string en Python list
        user.save()

        messages.success(request, 'Votre compte a été mis à jour avec succès.')
        return redirect('Utilisateurs:profil', id=user.id)
    else:
        return render(request, 'Utilisateurs/update_account.html', {'user': request.user})
