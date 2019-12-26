from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.


def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    output = ', '.join([q.question_text for q in latest_questions])
    return HttpResponse(output)

'''views with question number you're currently on'''
def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    response = "You're viewing results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
