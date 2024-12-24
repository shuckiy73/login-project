from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from todo import views

# Создаем маршрутизатор для API
router = routers.DefaultRouter()
router.register(r'acceptUser', views.AcceptUser, 'accept')

urlpatterns = [
    # Админ-панель Django
    path('admin/', admin.site.urls),

    # Включаем маршруты из приложения todo
    path('api/', include('todo.urls')),

    # Маршрут для обработки запросов к API
    path('api/acceptUser/', views.AcceptUser.as_view(), name='accept_user'),

    # Маршрут для обработки всех остальных запросов (React)
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]