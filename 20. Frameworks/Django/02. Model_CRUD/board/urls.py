from django.urls import path
from . import views

# namespace 설정
app_name = 'board'

# 앞 주소 /board +
# 고정값 > 변수값 순서로 쓰자., <str:>타입이면 new가 아닌 new 변수로 잡아버림
urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<pk>/', views.detail, name='detail'),
    path('<pk>/edit/', views.edit, name='edit'),
    path('<pk>/update/', views.update, name='update'),
    path('<pk>/delete/', views.delete, name='delete'),
]
'''
C
/board/new/
/board/create/
R
/board/
/board/1/
U
/board/1/edit
/board/1/update
D
/board/1/delete
'''