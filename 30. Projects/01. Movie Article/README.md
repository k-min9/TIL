# Movie Article



## 0. 배경

프론트로 부트스트랩, 백으로 장고를 배웠으니, 

둘을 합쳐서 영화 리스트를 보고 평가를 남기는 페이지를 만들어보자.





## 99. 작업기록

0. 기초작업

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

