from django.shortcuts import render
from datetime import datetime
from commondatab.models import ZzDiscussions
from commondatab.models import ZzUsersDiscussions
from commondatab.models import ZzMessages
from commondatab.models import ZzUsers
import json
from django.http import JsonResponse
import pytz

# Create your views here.

# Soit 1 l'id de l'utilisateur en session

def discussions (request, discID):
    userID = request.session.get('user')
    user_Message = []
    discussionsID = []
    if ZzDiscussions.objects.filter(id = discID).exists():
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

    actif = ZzUsersDiscussions.objects.filter(discussion_id = discID).exclude(user_id = userID).get()
    userActif = ZzUsers.objects.filter(id = actif.user_id).get()


    return render(request, 'chat/messagerie.html', {"user_Message" : user_Message, "actif" : userActif})


def send(request, disc):
    if request.method == 'POST':
        try:
            user = request.session.get("user")
            data = json.loads(request.body)
            disc = data['disc']
            content = data["message"]
            if(content):  
                if(ZzUsersDiscussions.objects.filter(user_id = user, discussion_id = disc).exists()):
                    tz = pytz.timezone('Africa/Porto-Novo')
                    date = datetime.now(tz)
                    newMessage = ZzMessages.objects.create(content = content, discussion_id = disc, user_id = user, created_at = date)
                    newMessage.save()
                    user_discussion = ZzUsersDiscussions.objects.filter(user_id = user, discussion_id = disc)
                    lastID = newMessage.id
                    discussion =  ZzDiscussions.objects.get(id = disc)
                    discussion.last_message_id = lastID
                    discussion.save()
                    response_data = {'status': 'success'}
        except json.JSONDecodeError:
            response_data = {'status': 'error', 'message': 'Invalid JSON data'}
    else:
        response_data = {'status': 'error', 'message': 'Expected a POST request'}
    return JsonResponse(response_data)


def getMessages(request, disc, lastID):
    user = request.session.get("user")
    if not ZzUsersDiscussions.objects.filter(user_id=user, discussion_id=disc).exists():
        return JsonResponse({"deja": "0"})
    if lastID != 0:
        messages = ZzMessages.objects.filter(discussion_id=disc, id__gt = lastID).order_by("created_at")
    else:
        messages = ZzMessages.objects.filter(discussion_id=disc).order_by("created_at")

    if messages.exists():
        data = {
            "messages": list(messages.values()),  # Convertir QuerySet en liste de dictionnaires JSON
            "sender": user,
            "receiver_img": "http://localhost:8000/static/image/profile.jpg",
            "sender_img": "http://localhost:8000/static/image/profile.jpg"  
        }
        return JsonResponse(data)
    else:
        return JsonResponse({"deja": "0"})
    
def isoFormatDate(timestamp):
    timestamp = int(timestamp)
    dt = datetime.fromtimestamp(timestamp)
    return dt.isoformat()
