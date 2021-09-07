from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from .models import Article
from .forms import ArticleForm


@require_http_methods(['GET', 'POST'])
def create(request):
    # 5. 사용자가 데이터를 입력 & POST /articles/create/ => invalid data
    # 10. 사용자가 데이터를 입력 & POST /articles/create/ => valid data
    if request.method == 'POST':
        # 6. 데이터를 검증할 ArticleForm 인스턴스 초기화 => 내용 있음
        # 11. 데이터를 검증할 ArticleForm 인스턴스 초기화 => 내용 있음
        form = ArticleForm(request.POST)
        # 7. 검증 => 실패
        # 12. 검증 => 성공
        if form.is_valid():
            # 13. form 을 통해 데이터 저장
            article = form.save()  
            # 14. /articles/<pk>/ 로 redirect 하도록 응답
            return redirect('articles:detail', article.pk)
    # 1. GET /articles/create/ => 빈 form 요청
    else:
        # 2. 비어있는 ArticleForm 인스턴스를 초기화 => 빈 form 생성
        form = ArticleForm()

    # 3. 빈 form 을 context에 담음
    # 8. 에러 메시지를 담은 form을 context에 담음
    context = {'form': form, 'page_name': 'Create'}

    # 4. 사용자에게 빈 form 제공
    # 9. 에러 미시지를 포함한 form 제공
    return render(request, 'articles/form.html', context)


@require_safe
def index(request):
    # pk 내림차순 정렬
    articles = Article.objects.order_by('-pk')
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


@require_safe
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()              
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'article': article,
        'form': form,
        'page_name': 'Update',
    }
    return render(request, 'articles/form.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
