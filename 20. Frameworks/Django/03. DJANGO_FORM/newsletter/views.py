from django.shortcuts import render
from .forms import MailForm

"""
Form 의 역할
1. validation
2. HTML
"""
from IPython import embed

def ping(request):
    # form 보내주기
    form = MailForm()  # HTML
    context = {
        'form': form,
    }
    return render(request, 'newsletter/ping.html', context)


def pong(request):
    form = MailForm(request.POST)  # 검증 (+ HTML)
    if form.is_valid():
        send_mail(
            title=form.cleaned_data['title'],
            content=form.cleaned_data['content']
        )
 