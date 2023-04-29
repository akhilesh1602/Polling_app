from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
from main import models

class Index(ListView):
    model = models.Question
    template_name = 'main/index.html'
    # context_object_name = 'question_list' (lowercase modelname)

class Question(DetailView):
    model = models.Question
    template_name = 'main/question.html'
