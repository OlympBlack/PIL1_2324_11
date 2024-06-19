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

