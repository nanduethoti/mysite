from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list=Question.objects.order_by('pub_date')[:5]
    """output=','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)"""
    context={'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)
def detail(request,question_id):
    #return HttpResponse("you are looking at the question %s"%question_id)
    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def result(request,question_id):
    respomse="you are looking ar the results of question %s."
    return HttpResponse(respomse %question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on %s" %question_id)

