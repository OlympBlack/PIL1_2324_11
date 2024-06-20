from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from commondatab.models import ZzFriendship
from commondatab.models import ZzDiscussions
from commondatab.models import ZzUsersDiscussions
from commondatab.models import ZzUsers

from datetime import datetime
from django.contrib.auth.decorators import login_required

#@login_required
"""def acceuil(request):
    zzuser = request.user
    context = {'zzuser': zzuser}
    return render(request, 'acceuil/index.html', context)"""

def acceuil(request, *args, **kargs):
    request.session["user"] = 1
    
    return render(request, 'acceuil/index.html')


def saveLike(request, liker, liked):
    if request.method == 'POST':
        try:
            user = request.session.get("user")
            if(ZzUsers.objects.filter(id__in = (liked, liker)).exists()):
                data = json.loads(request.body)
                if(user == liker):
                    lik = ZzFriendship.objects.filter(liked = liked)
                    if(lik.exists()):
                        if(lik.lik):
                            lik.update(liker_like = 1)
                            lik.update(liker = liker)
                            discussion = ZzDiscussions.objects.create()
                            discussion.save()
                            discussion_id = discussion.id
                            lien1 = ZzUsersDiscussions.objects.create(status = 1, discussion_id = discussion_id, user_id = liked)
                            lien1.save()
                            lien2 = ZzUsersDiscussions.objects.create(status = 1, discussion_id = discussion_id, user_id = liker)
                            lien2.save()
                        else: 
                            lik.update(liker_like = 1)
                            lik.update(liker = liker)
                    else:
                        lik = ZzFriendship.objects.create(liked = liker, lik = 1)
                        lik.save()   
                    response_data = {'status': 'success'}
        except json.JSONDecodeError:
                response_data = {'status': 'error', 'message': 'Invalid JSON data'}
    else:
        response_data = {'status': 'error', 'message': 'Expected a POST request'}
        return JsonResponse(response_data)

def deleteLike(request, liker, liked):
    if request.method == 'POST':
        try:
            user = request.session.get("user")
            if(ZzUsers.objects.filter(id__in = (liked, liker)).exists()):
                data = json.loads(request.body)
                if(user == liker):
                    lik = ZzFriendship.objects.filter(liked = liked)
                    if(lik.exists()):
                        if(lik.lik):
                            lik.update(liker_like = 0)
                            lik.update(liker = liker)
                        else:
                            lik.delete(lik)
                    else:
                        lik = ZzFriendship.objects.create(liked = liker, lik = 0)
                        lik.save()   
                    response_data = {'status': 'success'}
                else:
                    response_data = {'status': 'error', 'message': 'Invalid JSON data'}     
        except json.JSONDecodeError:
                response_data = {'status': 'error', 'message': 'Invalid JSON data'}
    else:
        response_data = {'status': 'error', 'message': 'Expected a POST request'}
        return JsonResponse(response_data)
