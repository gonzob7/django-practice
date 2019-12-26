from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question
# Create your views here.


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_questions':latest_questions}
    return render(request, 'polls/index.html', context)

'''views with question number you're currently on'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Error: Question does not exist")

    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You're viewing results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
