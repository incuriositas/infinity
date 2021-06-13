from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('main/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))


def score(request):
    template = loader.get_template('main/tables.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('main/register.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
