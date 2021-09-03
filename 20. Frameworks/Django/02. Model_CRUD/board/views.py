from django.shortcuts import render, redirect
from .models import Question

# Create
# 데이터 제출 폼 제공(html)
def new(request):
    # 무조건 첫 인자 request, 다음은 조회할 필요가 있을 경우 html
    return render(request, 'board/new.html')

# 제출 데이터 저장
def create(request):
    question = Question()
    # request.POST['title'] 안 씀
    # 키 값을 못 찾을때 None을 반환하는 get (딕셔너리)함수를 사용한다. 
    question.title = request.POST.get('title')
    question.category = request.POST.get('category')
    question.content = request.POST.get('content')
    question.save()
    #return redirect(f'/board/{question.pk}/') << 하드코딩 ㄴㄴ해
    return redirect('board:detail', question.pk)

# Read
# 전체 목록 조회(html)
def index(request):
    questions = Question.objects.all()
    # 키값이 questions로 내용물을 딕셔너리에 담는다.
    context = {
        'questions' : questions,
    }
    return render(request, 'board/index.html', context)

# 단일 목록 조회(html)
def detail(request, pk):
    question = Question.objects.get(pk = pk)
    context = {
        'question' : question,
    }
    return render(request, 'board/detail.html', context)

# Update
# 데이터 수정 폼 제공(html + 기존내용 있음)
def edit(request, pk):
    question = Question.objects.get(pk = pk)
    context = {
        'question' : question,
    }
    return render(request, 'board/edit.html', context)

# 수정 데이터를 기존 내용에 변경, 저장
def update(request, pk):
    # 우선 기존거 찾고
    question = Question.objects.get(pk = pk)

    # 내용 업데이트
    question.title = request.POST.get('title')
    question.category = request.POST.get('category')
    question.content = request.POST.get('content')
    question.save()
    
    # 마찬가지로 리다이렉트
    return redirect('board:detail', question.pk)

# Delete
# 단일 데이터 삭제
def delete(request, pk):
    # 정상적인 요청
    if request.method == 'POST':
        # 우선 기존거 찾고
        question = Question.objects.get(pk = pk)
        # 지우고
        question.delete()
        # 마찬가지로 리다이렉트 (목록으로 보내자)
        return redirect('board:index')
    else:
        return redirect('board:detail')