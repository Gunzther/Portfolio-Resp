from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from .models import Question
from .forms import QuestionForm


def get_questions(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'questions/questions.html', context)


def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = Question(name=form.cleaned_data['your_name'], email=form.cleaned_data['your_email'],
                                    question_text=form.cleaned_data['your_question'], pub_date=timezone.now())
            new_question.save()

    form = QuestionForm()
    return render(request, 'portfolio/index.html', {'form': form})
