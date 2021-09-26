# Movie Article



## 0. 배경

프론트로 부트스트랩, 백으로 장고를 배웠으니, 

둘을 합쳐서 영화 리스트를 보고 평가를 남기는 페이지를 만들어보자.



## 98. 궁금증

이미 만들어진 프로젝트 이름 바꾸는 법.



## 99. 작업기록

### 0. 기초작업

```
python -m venv venv
source venv/scripts/activate
pip install django, django-extensions
pip freeze>requirements.txt
(차후, pip install -r requirements.txt)
```

gitgnore 세팅해두고, 프로젝트 시작.

```
djano-admin startproject Movie
```

복수의 프로젝트를 만들 생각은 없으므로 프로젝트 상단으로 옮기고 venv 다시 활성화, application 추가

```
source venv/scripts/activate
python manage.py startapp accounts
python manage.py startapp community
```

migrations와 migrate 체크하면 준비 끝

```
python manage.py makemigrations
python manage.py migrate
```



### 1. 프로젝트 설정

일단 추가한 설정에 맞게 settings.py 기본 세팅

```
INSTALLED_APPS = [
    #local apps
    'accounts',
    'community',

    # 3rd party apps
    'dango_extensions',
	
	...
]
```

```
TEMPLATES = [
    {
    	...
        'DIRS': [BASE_DIR/'templates'],
        ...
    },
]
```

```
LANGUAGE_CODE = 'ko-kr'
```



프로젝트의 urls.py에 기본 설정

```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls'))
```



부트스트랩 추가.

방법1) 라이브러리

```
1. pip install django-bootstrap-v5
2. INSTALLED_APPS = [
    # 3rd party apps
    'dango_extensions',
    ]
    추가
3. 사용할 html에 {%load bootstrap}
```

방법2) CDN

사용할 html <head\>에

```
<!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
```

사용할 html \<body>에

```
 <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
```



방법3) CSS 직접 사용 (이번 프로젝트는 이것 채택)

프로젝트 최상단에 static 폴더 만들고, css폴더 내에 bootstrap.min.css 파일, js 폴더내에 bootstrap.min.js 파일 집어 넣기

프로젝트 최상단에 templates 폴더 만들고, base.html 생성

\<head>에

```
{% load static %}
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
```

\<body>에

```
<script src="{% static 'js/bootstrap.min.js' %}"></script>
```









### 2. Community

