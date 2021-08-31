from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    # 'first_app
    path('hello/', views.hello, name='hello'), #밑에 variable routing 하는 순간 기본값 안 넣어주면 망가짐, 넣어주면 문제 없음
    path('hello/<name>/',views.hello, name = 'lunch'),
    path('lunch/', views.lunch, name = 'lunch'),
    path('lotto/', views.lotto, name = 'lotto'),
    path('ping/', views.ping, name = 'ping'),
    path('pong/', views.pong, name = 'pong'),
]