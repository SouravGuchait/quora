from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm, RegisterForm

@login_required
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions/question_list.html', {'questions': questions})

@login_required
def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'questions/question_detail.html', {'question': question, 'answers': answers, 'form': form})

@login_required
def new_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'questions/new_question.html', {'form': form})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    Like.objects.get_or_create(answer=answer, user=request.user)
    return redirect('question_detail', id=answer.question.id)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})