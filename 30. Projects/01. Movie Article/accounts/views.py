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