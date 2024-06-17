from django.shortcuts import render#, redirect, get_object_or_404
from django.http import HttpResponse
"""from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User"""
from commondatab.models import ZzUsers
"""from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages

import os
from dotenv import load_dotenv

load_dotenv()"""

def Index(request):
    return render(request, "Utilisateurs/index.html")


def Inscription(request):
    """if request.method=='POST':
        pseudo=request.POST['pseudo']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        sexe=request.POST['sexe']
        preference=request.POST['preference']
        birthday=request.POST['birthday']
        if password1 != password2:
            messages.error(request, 'Les mots de passes ne correspondent pas')
            #return render(request, "Utilisateurs/inscription.html")
        
        elif ZzUsers.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà")
            #return render(request, "Utilisateurs/inscription.html")
        else:
            user=ZzUsers.objects.create_user(pseudo=pseudo, email=email, password=password1, sex=sexe, pref=preference, birthday=birthday)
            user.is_active = False 
            user.save()
            token = default_token_generator.make_token(user)
            user.confirmation_token = token
            user.save()
            
            current_site = get_current_site(request)

            send_mail(
                f"Welcome to SoulQuest {user.pseudo}",
                'Thank you for registering on our site.',
                os.getenv('EMAIL_HOST_USER'),
                [user.email],
                fail_silently=False,
            )
            subject = 'Confirmation de votre compte'
            message = render_to_string('Utilisateurs/confirmation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'token': token,
            })
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return redirect('Utilisateurs:confirmation_sent')"""  # Rediriger vers une page de confirmation envoyée
    return render(request, 'Utilisateurs/inscription.html')

"""def confirm_account(request, token):
    user = get_object_or_404(ZzUsers, confirmation_token=token)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.confirmation_token = None
        user.save()
        return render(request, 'Utilisateurs/account_confirmed.html')
    else:
        return render(request, 'Utilisateurs/confirmation_invalid.html')"""

"""def confirmation_sent(request):
    return render(request, 'Utilisateurs/confirmation_sent.html')"""

def Connexion(request):
    
    return render(request, 'Utilisateurs/connexion.html')

def Profil(request):
    return render(request, 'Utilisateurs/profil.html')

