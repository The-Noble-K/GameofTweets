from django.shortcuts import render
from gotweet.models import Gotweet

def feed(request):
    userids = []
    for id in request.user.gotwitterprofile.follow.all():
        userids.append(id)

    userids.append(request.user.id)
    gotweets = Gotweet.objects.filter(user_id__in=userids)[0:25]

    return render(request, 'feed.html', {'gotweets': gotweets})


