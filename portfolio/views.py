from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.template import loader
from django.shortcuts import render


def index(request):
    return render(request, 'portfolio/index.html')


def get_questions(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions/questions.html', context)
