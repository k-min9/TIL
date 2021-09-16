# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # CREATE
    path('signup/', views.signup, name='signup'),
    # UPDATE
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # DELETE
    path('delete/', views.delete, name='delete'),
    
    # AUTHORIZATIONS    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # READ
    path('<str:username>/', views.profile, name='profile'),
]
