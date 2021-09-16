from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'articles/index.html')


@login_required
def new(request):
    # request.user => 인증됨 => User 의 instance => is_authenticated == True
    # request.user => 인증안됨 => AnonymousUser 의 instance => is_authenticated == False
    # if request.user.is_authenticated:
    
    return render(request, 'articles/new.html')
    