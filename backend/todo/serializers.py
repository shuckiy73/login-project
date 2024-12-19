from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
        # Добавляем verbose_name для полей
        extra_kwargs = {
            'id': {'label': 'ID'},
            'title': {'label': 'Заголовок'},
            'description': {'label': 'Описание'},
            'completed': {'label': 'Завершено'},
        }