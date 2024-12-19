
# todo/views.py

from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer      # add this
from .models import Todo  
from .models import TodoUser
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def AcceptUser(request):
  body_unicode = request.body.decode('utf-8')
  body = json.loads(body_unicode)
  try:
    tmp = TodoUser.objects.get(Q(username = body['username']) & Q(password = body['password']))
  except ObjectDoesNotExist:
    tmp = None
  sendMessage = ""
  if tmp == None:
    sendMessage = "Faild"
  else:
    sendMessage = "Success"
  return HttpResponse(sendMessage)