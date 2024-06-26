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
from django.views.generic import TemplateView
from django.views import View


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



"""from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from commondatab.models import ZzUsers
from django.urls import reverse
from django.views import View"""

def Index(request):
    return render(request, "Utilisateurs/index.html")

def Inscription(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        sexe = request.POST.get('sexe', '')
        city = request.POST.get('city', '')
        latitude = request.POST.get('latitude', '0')  # Default latitude value
        longitude = request.POST.get('longitude', '0')  # Default longitude value
        birthday_str = request.POST.get('birthday', None)

        if birthday_str:
            try:
                birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date()
            except ValueError:
                birthday = None
        else:
            birthday = None

        profile_media = request.FILES.get('profile_media')

        if not pseudo:
            messages.error(request, 'Le pseudo est requis')
            return render(request, 'Utilisateurs/inscription.html')

        if ZzUsers.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà")
            return render(request, 'Utilisateurs/inscription.html')

        user = ZzUsers.objects.create(
            email=email,
            pseudo=pseudo,
            password=make_password(password1),
            sex=sexe,
            city=city,
            latitude=latitude,
            longitude=longitude,
            birthday=birthday,
            profile_media=profile_media,
        )
        user.save()

        authenticated_user = authenticate(request, email=email, password=password1)
        if authenticated_user is not None:
            login(request, authenticated_user)
            request.session['new_user'] = True
            request.session["user"] = user.id
            return redirect(reverse('Utilisateurs:profil', kwargs={'id': user.id}))

    return render(request, 'Utilisateurs/inscription.html')
def Connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = user.id
            return redirect('acceuil') 
        else:
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')
            return render(request, 'Utilisateurs/connexion.html')
    
    return render(request, 'Utilisateurs/connexion.html')

@login_required
def profil(request, id):
    user = get_object_or_404(ZzUsers, pk=id)
    new_user = request.session.pop('new_user', False)
    context = {'user': user, 'new_user': new_user}
    return render(request, 'Utilisateurs/profil.html', context)

@login_required
def Logout(request):
    logout(request)
    return redirect('Utilisateurs:connexion')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Votre compte a été supprimé avec succès.')
        logout(request)
        return redirect('Utilisateurs:index') 

@login_required
def update_account(request):
    if request.method == 'POST':
        user = request.user

        email = request.POST.get('email', 'aucun')
        pseudo = request.POST.get('pseudo', 'aucun')
        nom = request.POST.get('nom', 'aucun')
        prenom = request.POST.get('prenom', 'aucun')
        password = request.POST.get('password', 'aucun')
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
        user.save()

        messages.success(request, 'Votre compte a été mis à jour avec succès.')
        return redirect('Utilisateurs:profil', id=user.id)
    else:
        return render(request, 'Utilisateurs/update_account.html', {'user': request.user})

def welcome_view(request):
    print("La vue de bienvenue a été appelée")  # Message de debug
    return render(request, 'welcome.html', context={'message': 'Bienvenue!'})

class ProfileView(View):
    def get(self, request):
        # Logique pour gérer la requête GET
        return render(request, 'profile.html')
    
# afficher le profil des autres utilisateurs
def orther_profil(request, id):
    orther_user = ZzUsers.objects.get(pk=id)
    context = {'orther_user': orther_user}
    return render(request, 'Utilisateurs/autre_profil.html', context)