from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, JsonResponse
from contact.models import Messages,Subscription
import json

# Create your views here.
def savemessage(request):
    if request.method == 'POST':
        if json.loads(request.POST['contactsave']):
            Messages.objects.create(
                Name=json.loads(request.POST['contactname']),
                Email=json.loads(request.POST['contactemail']),
                MsgSubject=json.loads(request.POST['contactsubject']),
                MsgBody=json.loads(request.POST['contactmessage'])
            )
            return JsonResponse({
                'message':'Message Sent Successfully'
            })


def getsubscriber(request):
    if request.method == 'POST':
        if json.loads(request.POST['usersubscribe']):
            semail = json.loads(request.POST['SubcriberEmail'])
            sname = json.loads(request.POST['SubcriberName'])
            if Subscription.objects.filter(SubcriberEmail__iexact=semail).exists():
                return JsonResponse({
                    'message': 'You already subscribed for news article'
                })
            else:
                Subscription.objects.create(
                    SubcriberEmail=semail,
                    SubcriberName=sname
                )
                return JsonResponse({
                    'message': 'Thank You for Subscribtion'
                })

