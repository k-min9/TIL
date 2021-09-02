from django.shortcuts import render, redirect
from .models import Article

# Create
# 사용자에게 <form> 포함한 html을 전송
def new(request):
    return render(request, 'articles/new.html')


# 사용자가 제출한 데이터를 '새로' 저장 => 상세페이지로 이동
def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content') 
    article.save()
    return redirect('articles:detail', article.pk)
    

# Read
# 전체 게시글 목록 조회
def index(request):
    # 게시글들(articles) 불러오기? => DB에서 가져오기 => DB와 통신? => Model!
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 특정 게시글 상세 조회
def detail(request, pk):
    # 단일 게시글(article)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# Update
# 사용자에게 <form> 포함한 html을 전송(+ 내용 채워서)
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


# 사용자가 제출한 데이터를 '기존' article에 저장 => 상세페이지로 이동
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content') 
    article.save()
    return redirect('articles:detail', article.pk)


# Delete => 목록 페이지로 redirect
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
    