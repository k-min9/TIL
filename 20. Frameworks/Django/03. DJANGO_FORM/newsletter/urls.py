from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'newsletter'

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('pong/', views.pong, name='pong'),
]
