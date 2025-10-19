from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='axion_v1_home'),
    path('chat/', views.chat, name='axion_v1_chat'),
]

