"""template_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.http.response import HttpResponse

from first_app import views

# views.py로 이동 >> 분리
# def hello(request):
#     #return 'Hello'
#     html = '<h1>Hello!</h1>'
#     return HttpResponse(html)

app_name = 'first_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('lunch/', views.lunch),

    # 반복 되는 주소 등등 처리하기
    path('first_app/', include('first_app.urls')),

]
