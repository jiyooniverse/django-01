from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice

# Create your views here.
def index(request):
    # Question 테이블에서 날짜 내림차순으로 데이터를 읽어온다..(최근 5개의 투표만)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)    
    if request.POST.get('choice'):
        selected_choice = question.choice_set.get(pk=request.POST.get('choice'))
        selected_choice.votes += 1
        question.total += 1
        question.save()
        selected_choice.save()
        return redirect('polls:results', question.pk)
    
    return redirect('polls:detail', question.pk)


