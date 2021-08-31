from django.http.response import HttpResponse
from django.shortcuts import render

import random

def hello(request, name = 'world'):

    context = {
        'name' : name
    }

    return render(request, 'first_app/hello.html', context)

def lunch(request):
    menus = ['백반', '샌드위치', '짜장면', '굶기']
    menu = random.choice(menus)
    # html = f'<h1>{menu}</h1>'
    # return HttpResponse(html)
    
    # lunch.html을 넘기자 (딕셔너리를 context로 3번째 인자로 보냄)
    return render(request, 'first_app/lunch.html', {'menu' : menu})

def lotto(request):
    numbers = random.sample(range(1,46),6)

    context = {
        'numbers' : numbers,
        }

    return render(request, 'first_app/lotto.html', context)
    
def ping(request):
    # 사용자에게 form이 담긴 html 제공
    return render(request, 'first_app/ping.html')

def pong(request):
    # ping에서 여기로 날아올 예정

    print(f'>>>>>>>> {request.GET}')

    context = {
        'a': request.GET['message'],
        'b': request.GET['sign'],
        # 사인 미 입력시 에러는 안터지게 하는 법 
        # 'b': request.GET.get('sign', '기본값'),
    }
    return render(request, 'first_app/pong.html', context)

