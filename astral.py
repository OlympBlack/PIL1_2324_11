#utils.py#

from datetime import date

def get_astrological_sign(birthdate):
    astro_signs = [
        ("Capricorne", (1,1), (1,19)),
        ("Verseau", (1,20), (2,18)),
        ("Poissons", (2,19), (3,20)),
        ("Bélier", (3,21), (4,19)),
        ("Taureau", (4,20), (5,20)),
        ("Gémeaux", (5,21), (6,20)),
        ("Cancer", (6,21), (7,22)),
        ("Lion", (7,23), (8,22)),
        ("Vierge", (8,23), (9,22)),
        ("Balance", (9,23), (10,22)),
        ("Scorpion", (10,23), (11,21)),
        ("Sagittaire", (11,22), (12,21)),
        ("Capricorne", (12,22), (12,31)),
        
    ]
    
    for sign, start, end in astro_signs:
        start_date = date(birthdate.year, start[0], start[1])
        end_date = date(birthdate.year, end[0], end[1])
        if start_date <= birthdate <= end_date:
            return sign
        return None
    

#views.py#

from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .utils import get_astrological_sign

def astrological_sign_view(request):
    if request.method == POST:
        birthdate_str = request.POST.get(birthdate)
        try:
            birthdate = datetime.str ptime(birthdate_str, '%Y-%m-%d').date()
            sign = get_astrological_sign(birthdate)
            return JsonResponse({"astrological_sign": sign})
        except ValueError:
            return JsonResponse({'error': 'invalid date format. Please use YYYY-MM-DD.'}, status= 400)
    return render(request, 'astrology/birthdate_form.html')


#models.py#

from django.db import models
from django.contrib.auth.models import User
from .utils import get_astrological_sign

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    birthdate = models.DateField()
    astrological_sign = models.CharField(max_length= 20, blank= True)
    
    def save(self, *args, **kwargs):
        if self.birthdate:
            self.astrological_sign = get_astrological_sign(self.birthdate)
        super(UserProfile, self).save(*args, **kwargs)
        