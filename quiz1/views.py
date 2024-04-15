from django.shortcuts import render, redirect
from django.views import generic

from .forms import QuizForm
from .models import Question, Choice, UserAnswer


class IndexView(generic.TemplateView):
    template_name = "index.html"


def question(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            choice_id = form.cleaned_data.get('choice')
            choice = Choice.objects.get(id=choice_id)
            UserAnswer.objects.create(question=question, selected_choice=choice)
            return redirect('result', question_id=question_id)
    else:
        form = QuizForm()
    return render(request, 'question.html', {'form': form, 'question': question})


def result(request, question_id):
    question = Question.objects.get(id=question_id)
    user_answer = UserAnswer.objects.get(question=question)
    return render(request, 'result.html', {'question': question, 'user_answer': user_answer})
