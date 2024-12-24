from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo  # Импортируйте модель из models.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import TodoUser  # Убедитесь, что модель TodoUser импортирована

class AcceptUser(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            # Проверяем, существует ли пользователь с указанными данными
            tmp = TodoUser.objects.get(Q(username=username) & Q(password=password))
        except ObjectDoesNotExist:
            tmp = None

        if tmp is None:
            return Response({'message': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)