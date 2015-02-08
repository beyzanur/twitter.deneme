from django.shortcuts import render_to_response
from django . http import *
from denemek.models import *
from django.views.decorators.csrf import csrf_exempt
from django import template
def merhaba_dunya(request):
    #variable = "beyzanur kocak"
    tweetler = Tweet.objects.all()
    return render_to_response("text.html", locals())

@csrf_exempt
def gonder(request):
    if request.method == "POST":
        twittertext = request.POST.get("tweet")
        twittercount = request.POST.get("rt")
        register_tweet=Tweet(tweet_text=twittertext, rt_count=twittercount)
        register_tweet.save()
        return HttpResponse(u"kayit basarili: %s" %twittertext )
    else:
        return HttpResponse(u"404")



