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

### 4. Home 페이지, Navbar, footer, Modal 제작

- base.html에 임시 navbar 비활성화, navbar, footer, Modal 추가

```
<!-- Navbar -->
<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <div class="container-fluid">

      <a class="navbar-brand" href="02_home.html">
        <img src="{% static './images/logo.png' %}" alt="logo" width="120" height="55">
      </a>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <li><a href="02_home.html" class="nav-link active text-decoration-none mx-2 text-end">Home</a></li>
          </li>
          <li class="nav-item ms-md-auto">
            <li><a href="03_community.html" class="nav-link text-decoration-none mx-2 text-end">Community</a></li>
          </li>
          <li class="nav-item ms-md-auto">
            <li><a href="#" class="nav-link text-decoration-none mx-2 text-end" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a></li>
          </li>
        </ul>
      </div>
    </div>
  </nav>
```

```
  <!-- Footer -->
  <footer class="d-flex fixed-bottom justify-content-center align-items-center">
    <p class="my-2 text-dark fw-bold">Django-bootsrtap PJT by 강민구</p>
  </footer>
```

```
  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form action="#" class="d-flex flex-column">
            <div>
              <label for="username">Username</label><br>
              <input class="form-control mb-2" id="username" type="text">
            </div>
            
            <div>
              <label for="password">Password</label><br>
              <input class="form-control mb-3" id="username" type="password">  
            </div>
            <div>
              <input type="checkbox"> Check me out
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Submit</button>
        </div>
      </div>
    </div>
  </div>
```

- project의 urls.py에 path 추가 후, views.py를 생성하여 사이트 접속시 무조건 home.html로 들어가게 설정

```
from . import views

path('', views.index, name='index'),
```

```
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')
```

- 기존 base.html의 container을 container-fluid로 바꾸고(양 끝이 꽉 참), home.html 생성

base.html 상속하더라도 static은 따로 load 해줘야 함

```
{% extends 'base.html' %}
{% load static %}

{% block content %}

  <header>
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="{% static './images/header1.jpg' %}" class="d-block w-100" alt="header1">
        </div>
        <div class="carousel-item">
          <img src="{% static './images/header2.jpg' %}" class="d-block w-100" alt="header2">
        </div>
        <div class="carousel-item">
          <img src="{% static './images/header3.jpg' %}" class="d-block w-100" alt="header3">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </header>

  <h1 class="text-center py-5 fw-bold">Boxoffice</h1>

  <article class="container">
    <div class="row mb-5 g-3">
      <div class="col-12 col-sm-6 d-flex justify-content-center">
        <div class="card">
          <img src="{% static './images/movie1.jpg' %}" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text"><strong>Movie Title</strong><br>This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </div>

      <div class="col-12 col-sm-6 d-flex justify-content-center">
        <div class="card">
          <img src="{% static './images/movie2.jpg' %}" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text"><strong>Movie Title</strong><br>This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </div>

      <div class="col-12 col-sm-6 d-flex justify-content-center">
        <div class="card">
          <img src="{% static './images/movie3.jpg' %}" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text"><strong>Movie Title</strong><br>This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </div>

      <div class="col-12 col-sm-6 d-flex justify-content-center">
        <div class="card">
          <img src="{% static './images/movie4.jpg' %}" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text"><strong>Movie Title</strong><br>This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </div>

      <div class="col-12 col-sm-6 d-flex justify-content-center">
        <div class="card">
          <img src="{% static './images/movie5.jpg' %}" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text"><strong>Movie Title</strong><br>This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </div>

      <div class="col-12 col-sm-6 d-flex justify-content-center">
        <div class="card">
          <img src="{% static './images/movie6.jpg' %}" class="card-img-top" alt="...">
          <div class="card-body">
            <p class="card-text"><strong>Movie Title</strong><br>This is a longer card with supporting text below as...</p>
          </div>
        </div>
      </div>
    </div>

{% endblock content %}
```

