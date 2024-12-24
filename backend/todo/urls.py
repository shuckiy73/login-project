from django.urls import path
from . import views

urlpatterns = [
    # Пример маршрута
    path('acceptUser/', views.AcceptUser.as_view(), name='accept_user'),
]