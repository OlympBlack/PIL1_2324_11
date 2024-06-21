from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import template
import json
from django.http import JsonResponse
from commondatab.models import ZzFriendship
from commondatab.models import ZzDiscussions
from commondatab.models import ZzUsersDiscussions
from commondatab.models import ZzUsers
from commondatab.models import ZzMessages
from datetime import date
from django.contrib import messages


from datetime import datetime
from django.contrib.auth.decorators import login_required

#@login_required
"""def acceuil(request):
    zzuser = request.user
    context = {'zzuser': zzuser}
    return render(request, 'acceuil/index.html', context)"""
@login_required
def acceuil(request, *args, **kargs):
    userID = request.session.get('user')
    user_Message = []
    discussionsID = []

    if ZzUsersDiscussions.objects.filter(user_id = userID).exists():
        users = ZzUsersDiscussions.objects.filter(user_id = userID)
        for useri in users:
            discussionsID.append(useri.discussion_id)
        print(discussionsID)    
        for renderDisc in discussionsID:
            discussions = ZzDiscussions.objects
            message = ZzMessages.objects
            messages = ZzMessages.objects.filter(discussion = renderDisc)
            if(len(messages) > 0):
                lastMessage = messages[len(messages)-1].content
            else:
                lastMessage = ""    
            Interlo = ZzUsersDiscussions.objects.filter(discussion_id = renderDisc).exclude(user_id = userID).get()
            print("Je suis interlo ",Interlo.id)
            user_Message.append({
                1 : ZzUsers.objects.filter(id = Interlo.user_id).get(),
                2 : lastMessage,
                3 : Interlo.user_id
            })

    if(ZzUsers.objects.all().exists):
        All_users = ZzUsers.objects.exclude(id = userID).all()
    else:
        All_users = []  

    return render(request, 'acceuil/index.html', {'user_Message' : user_Message, 'All_users' : All_users, "userID" : userID})
    if request.method == 'GET':
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


def saveLike(request, liker, liked):
    if(ZzUsers.objects.filter(id__in = (liked, liker)).exists()):
        like1 = ZzUsers.objects.filter(id = liker).get().id
        like2 = ZzUsers.objects.filter(id = liked).get().id
        like1_user = ZzUsers.objects.filter(id = liker).get()
        like2_user = ZzUsers.objects.filter(id = liked).get()

        print(like1, like2)
        user = request.session.get("user")
        lik = ZzFriendship.objects.filter(liker = like2, liked = like1)
        if(user == like1):
            deja = ZzFriendship.objects.filter(liker = like1, liked = like2)
            if(deja.exists()):
                if(deja.get().lik == 1):
                    messages.success(request, "Vous avez déjà liker cette personne")
                    return redirect("/acceuil/?then=true")
                else:
                    up = ZzFriendship.objects.filter(liker = like1, liked = like2).get()
                    up.lik = 1
                    up.save()
                    if(lik.exists()):
                        if(lik.get().lik == 1):
                            discussion = ZzDiscussions.objects.create()
                            discussion.save()
                            discussion_id = discussion.id
                            lien1 = ZzUsersDiscussions.objects.create(status = 1, discussion_id = discussion_id, user_id = like2)
                            lien1.save()
                            lien2 = ZzUsersDiscussions.objects.create(status = 1, discussion_id = discussion_id, user_id = like1)
                            lien2.save()
                            message = "Vous pouvez maintenant discuter avec" + like2_user.pseudo
                            messages.success(request, message)
                            redirection = "/chat/disc/" + discussion_id+"?change="+str(like2)
                            return redirect(redirection)
                        else:
                            message = "Vous pouvez expérer que " + like2_user.pseudo+ " vous accepte"
                            messages.success(request, message)
                            redirection = "/acceuil/?expect="+str(like2)
                            return redirect(redirection)   
                    else :
                        message = "En attente de réponse de " + like2_user.pseudo
                        messages.success(request, message)
                        redirection = "/acceuil/?atempt="+str(like2)
                        return redirect(redirection)
            else:
                lik = ZzFriendship.objects.filter(liker = like2, liked = like1)
                if(lik.exists()):
                    if(lik.get().lik == 1):
                        discussion = ZzDiscussions.objects.create()
                        myLike = ZzFriendship.objects.create(liker = like1_user, lik = 1, liked = like2_user)
                        myLike.save()
                        discussion.save()
                        discussion_id = discussion.id
                        lien1 = ZzUsersDiscussions.objects.create(status = 1, discussion_id = discussion_id, user_id = like2)
                        lien1.save()
                        lien2 = ZzUsersDiscussions.objects.create(status = 1, discussion_id = discussion_id, user_id = like1)
                        lien2.save()
                        message = "Vous pouvez maintenant discuter avec " + like2_user.pseudo
                        messages.success(request, message)
                        redirection = "/chat/disc/" + discussion_id+"?accepte="+str(like2)
                        return redirect(redirection)
                    else:
                        message = "Vous pouvez expérer que " + like2_user.pseudo+ " vous accepte"
                        messages.success(request, message)
                        redirection = "/acceuil/?expect="+like2
                        return redirect(redirection)
                else:
                    message = "En attente de la réponse de " + like2_user.pseudo
                    messages.success(request, message)
                    redirection = "/acceuil/?atempt="+str(like2)
                    return redirect(redirection)
        else:
            message = "Nous vous prions de bien vouloir vous connecter"
            messages.success(request, message)
            return redirect("/acceuil/")#vue de co
    else:
        message = "Nous vous prions de bien vouloir vous connecter"
        messages.success(request, message)
        return redirect("/acceuil")

def deleteLike(request, liker, liked):
    if(ZzUsers.objects.filter(id__in = (liked, liker)).exists()):
        user = request.session.get("user")
        lik = ZzFriendship.objects.filter(liker = liked, liked = liker)
        if(user == liker):
            deja = ZzFriendship.objects.filter(liker = liker, liked = liked)
            if(deja.exists()):
                if(deja.get().lik == 0):
                    message = "Vous l'avez déjà disliké"
                    messages.success(request, message)
                    return redirect("/acceuil/?thenNo=true") #tu l'as déjà disliker
                else:
                    up = ZzFriendship.objects.filter(liker = liker, liked = liked).get()
                    up.lik = 0
                    up.save()
                    message = "Personne disliké!! Nous en tiendrons compte pour les prochaines suggestions"
                    messages.success(request, message)
                    redirection = "/acceuil/?atemptNo="+str(liked)
                    return redirect(redirection) #Nous en tiendrons compte pour les prochaines suggestion
            else:
                myLike = ZzFriendship.objects.create(liker = liker, lik = 0, liked = liked)
                myLike.save()
                message = "Personne disliké!! Nous en tiendrons compte pour les prochaines suggestions"
                messages.success(request, message)
                redirection = "/acceuil/?atemptNo="+str(liked)
                return redirect(redirection) #Nous en tiendrons compte pour les prochaines suggestion

        else:
            message = "Nous vous prions de bien vouloir vous connecter"
            messages.success(request, message)
            return redirect("/acceuil/")#vue de co
    else:
        message = "Nous vous prions de bien vouloir vous connecter"
        messages.success(request, message)
        return redirect("/acceuil")