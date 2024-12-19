from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo  # Импортируйте модель из models.py
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def AcceptUser(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        tmp = TodoUser.objects.get(Q(username=body['username']) & Q(password=body['password']))
    except ObjectDoesNotExist:
        tmp = None
    sendMessage = ""
    if tmp is None:
        sendMessage = "Faild"
    else:
        sendMessage = "Success"
    return HttpResponse(sendMessage)