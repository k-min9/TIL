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

- 일단 추가한 설정에 맞게 settings.py 기본 세팅

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



- 프로젝트의 urls.py에 기본 설정

```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls'))
```



- 부트스트랩 추가하기

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

settings.py에

```
STATICFILES_DIRS = [BASE_DIR / 'static',] 
```

추가



### 2. Community

MTV 순서대로 짜면 된다.

- models.py에 가서 클래스 선언

```
class Review(models.Model):
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

그 이후에 migrate 하기

```
python manage.py makemigrations
python manage.py migrate
```

- admin.py에 가서 admin 내용 추가

```
from .models import Review

admin.site.register(Review)
```

- forms.py 생성하고, 제약 조건에 맞는 Form 생성

```
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    movie_title = forms.CharField(max_length = 100)
    title = forms.CharField(max_length = 100)

    class Meta:
        model = Review
        fields = '__all__'
```

- urls.py를 생성하고, app_name 및 패턴을 선언한다.

```
from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
```

- view.py에 각각 urlpattern에 맞는 함수 생성 및 내용 채우기

```
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from .models import Review
from .forms import ReviewForm 
from django.contrib.auth.decorators import login_required

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('community:detail', article.pk)
    else:
        form = ReviewForm()
    context = {'form': form, }
    return render(request, 'community/form.html', context)


@require_safe
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_safe
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'community/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            article = form.save()
            return redirect('community:detail', article.pk)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
    }
    return render(request, 'community/form.html', context)

@login_required
@require_POST
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('community:index')
```

- templates>community 폴더 생성 후 detail.html, form.html, index.html 생성

```
#detail.html

{% extends 'base.html' %}

{% block content %}

  <h2>상세 내용</h2>
  <h3>{{ review.pk }}번째 글</h3>
  <hr>
  <p>글 번호 : {{ review.pk }}</p>
  <p>영화 제목 : {{ review.movie_title }}</p>
  <p>글 제목 : {{ review.title }}</p>
  <p>글 내용 : {{ review.content }}</p>
  <hr>

  <a href="{% url 'community:update' review.pk %}">[UPDATE]</a>
  <form action="{% url 'community:delete' review.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>

  <a href="{% url 'community:index' %}">[back]</a>
{% endblock content %}
```

```
# form.html

{% extends 'base.html' %}

{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'community:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성">
  </form>
  <a href="{% url 'community:index' %}">[back]</a>
{% endblock content %}
```

```
# index.html

{% extends 'base.html' %}

{% block content %}
  <h1>Review</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'community:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for review in reviews %}
    <p>글 번호 : {{ review.pk }}</p>
    <p>영화 제목 : {{ review.movie_title }}</p>
    <p>글 제목 : {{ review.title }}</p>
    <p>글 내용 : {{ review.content }}</p>
    <a href="{% url 'community:detail' review.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock content %}
```



### 3. accounts

community에서 로그인 전제라던가 쓰였으니 accounts 부터 작성해야 했다.

- urls.py를 생성하고, app_name 및 패턴을 선언한다.

```
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup' ),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

- view.py에 각각 urlpattern에 맞는 함수 생성 및 내용 채우기

```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user, login as auth_login, logout as auth_logout

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 가입 후 자동 로그인
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = UserCreationForm()

    context = {'form':form,}
    return render(request, 'accounts/signup.html', context)
            

def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html', context)
        

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')
```

- templates>accounts 폴더 생성 후 login.html, signup.html 생성

```
# login.html

{% extends 'base.html' %}

{% block content %}
<h1>Login</h1>
<form method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <button>로그인</button>
</form>

{% endblock content %}
```

```
#signup.html 

{% extends 'base.html' %}

{% block content %}
<h1>Signup</h1>
<form method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <button>회원가입</button>
</form>

{% endblock content %}
```



### 4. 정리

- base.html에 임시 navbar 활성화

```
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="{% url 'community:index' %}">LOGO</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'community:index' %}">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'community:create' %}">Create</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
```

- home.html을 만들어서 처음 킬 경우 무조건 거기로 가게 설정
