from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#@login_required
"""def acceuil(request):
    zzuser = request.user
    context = {'zzuser': zzuser}
    return render(request, 'acceuil/index.html', context)"""

@login_required
def acceuil(request):
    return render(request, 'acceuil/index.html', {'user': request.user})