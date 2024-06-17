from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dicussions (request, *args, **kargs):
    return render(request, 'chat/messagerie.html')
