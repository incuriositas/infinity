from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from .models import Problem


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


def problem1(request):
    p1_info = Problem.objects.filter(num=1)
    p1_info = p1_info[0]
    # template = loader.get_template('main/problem1.html')
    # context = {
    #     'latest_question_list': "test",
    # }
    # return HttpResponse(template.render(context, request))

    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p1_info.answer:
            return render(request, 'main/problem1.html', {'score': p1_info.score, 'flag': p1_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p1_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p1_info.score))
            return HttpResponseRedirect('/main/problem1')
        else:
            return render(request, 'main/problem1.html', {'score': p1_info.score, 'flag': "오답입니다"})

    return render(request, 'main/problem1.html', {'score': p1_info.score})


def problem2(request):
    p2_info = Problem.objects.filter(num=2)
    p2_info = p2_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p2_info.answer:
            return render(request, 'main/problem2.html', {'score': p2_info.score, 'flag': p2_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p2_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p2_info.score))
            return HttpResponseRedirect('/main/problem2')
        else:
            return render(request, 'main/problem2.html', {'score': p2_info.score, 'flag': "오답입니다"})

    return render(request, 'main/problem2.html', {'score': p2_info.score})


def problem3(request):
    p3_info = Problem.objects.filter(num=3)
    p3_info = p3_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p3_info.answer:
            return render(request, 'main/problem3.html', {'score': p3_info.score, 'flag': p3_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p3_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p3_info.score))
            return HttpResponseRedirect('/main/problem3')
        else:
            return render(request, 'main/problem3.html', {'score': p3_info.score, 'flag': "오답입니다"})

    return render(request, 'main/problem3.html', {'score': p3_info.score})


def problem4(request):
    p4_info = Problem.objects.filter(num=4)
    p4_info = p4_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p4_info.answer:
            return render(request, 'main/problem4.html', {'score': p4_info.score, 'flag': p4_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p4_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p4_info.score))
            return HttpResponseRedirect('/main/problem4')
        else:
            return render(request, 'main/problem4.html', {'score': p4_info.score, 'flag': "오답입니다"})

    return render(request, 'main/problem4.html', {'score': p4_info.score})


def problem5(request):
    template = loader.get_template('main/problem5.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
