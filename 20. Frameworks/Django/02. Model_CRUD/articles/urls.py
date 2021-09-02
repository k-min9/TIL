from django.urls import path
from . import views

app_name = 'articles'

# /articles/ +
urlpatterns = [
    # /articles/new/
    path('new/', views.new, name='new'),
    # /articles/create/
    path('create/', views.create, name='create'),
    # /articles/
    path('', views.index, name='index'),
    # /articles/1/
    path('<int:pk>/', views.detail, name='detail'),
    # /articles/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # /articles/1/update/
    path('<int:pk>/update/', views.update, name='update'),
    # /articles/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
]
