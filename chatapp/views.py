from django.shortcuts import render
from django.http import HttpResponse
from commondatab.models import ZzDiscussions
from commondatab.models import ZzUsersDiscussions
from commondatab.models import ZzMessages
import json
from django.http import JsonResponse


# Create your views here.

# Soit 1 l'id de l'utilisateur en session

def discussions (request, discID):
    request.session['user'] = 1
    userID = 1
    if ZzDiscussions.objects.filter(id = discID).exists():
        user1 = ZzUsersDiscussions.objects.get(user_id = userID, discussion_id = discID)
        user2 = ZzUsersDiscussions.objects.filter(discussion_id = discID).exclude(user_id = userID).get()

        messages = ZzMessages.objects.filter(user_id__in = (user1.user_id, user2.user_id)).filter(discussion_id = user1.discussion_id).order_by('created_at')
        """ print(messages[0].content)
        print(messages[0].user_id)
        print(user1.user_id) """
        context = {
            'disc' : discID,
            'user1': user1,
            'user2': user2,
            'messages': messages
        }

    return render(request, 'chat/messagerie.html', context)


def send(request, disc):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            disc = data['disc']
            content = data["message"]
            user = request.session.get("user")
            if(ZzUsersDiscussions.objects.filter(user_id = user, discussion_id = disc).exists()):
                newMessage = ZzMessages.objects.create(content = content, discussion_id = disc, user_id = user)
                newMessage.save()
            response_data = {'status': 'success'}
        except json.JSONDecodeError:
            response_data = {'status': 'error', 'message': 'Invalid JSON data'}
    else:
        response_data = {'status': 'error', 'message': 'Expected a POST request'}
    return JsonResponse(response_data)
