from django.contrib import admin
from .models import Todo  # Импортируем модель Todo

# Создаем класс для настройки отображения модели в админ-панели
class TodoAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке объектов
    list_display = ('title', 'description', 'completed')
    
    # Поля, по которым можно фильтровать объекты
    list_filter = ('completed',)
    
    # Поля, по которым можно выполнять поиск
    search_fields = ('title', 'description')
    
    # Поля, которые будут редактируемыми в списке объектов
    list_editable = ('completed',)
    
    # Поля, которые будут отображаться в деталях объекта
    fields = ('title', 'description', 'completed')

# Регистрируем модель Todo и настройки для нее
admin.site.register(Todo, TodoAdmin)