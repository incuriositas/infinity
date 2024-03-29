from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from .models import Problem
from django.contrib.auth.models import User
from score.models import Score


def index(request):
    # template = loader.get_template('main/index.html')
    # context = {
    #     'latest_question_list': "test",
    # }
    return render(request, 'main/index.html', {'username': request.user})


def problem1(request):
    p1_info = Problem.objects.filter(num=1)
    p1 = p1_info[0]

    # template = loader.get_template('main/problem1.html')
    # context = {
    #     'latest_question_list': "test",
    # }
    # return HttpResponse(template.render(context, request))

    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p1.answer:
            return render(request, 'main/problem1.html', {'score': p1.score, 'flag': p1.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p1.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p1.score))

            user = Score.objects.filter(user=request.user)
            if user:
                instance = user[0]
            else:
                instance = Score.objects.create(user=request.user)
            instance.problem.add(Problem.objects.get(num=1))
            problems = instance.problem.all()
            my_score = 0
            for p in problems:
                my_score += p.score
            print(my_score)

            return HttpResponseRedirect('/main/problem1')
        else:
            return render(request, 'main/problem1.html', {'score': p1.score, 'flag': "오답입니다", 'username': request.user})

    return render(request, 'main/problem1.html', {'score': p1.score, 'username': request.user})


def problem2(request):
    p2_info = Problem.objects.filter(num=2)
    p2 = p2_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p2.answer:
            return render(request, 'main/problem2.html', {'score': p2.score, 'flag': p2.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p2.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p2.score))

            user = Score.objects.filter(user=request.user)
            if user:
                instance = user[0]
            else:
                instance = Score.objects.create(user=request.user)
            instance.problem.add(Problem.objects.get(num=2))
            problems = instance.problem.all()
            my_score = 0
            for p in problems:
                my_score += p.score
            print(my_score)

            return HttpResponseRedirect('/main/problem2')
        else:
            return render(request, 'main/problem2.html', {'score': p2.score, 'flag': "오답입니다", 'username': request.user})

    return render(request, 'main/problem2.html', {'score': p2.score, 'username': request.user})


def problem3(request):
    p3_info = Problem.objects.filter(num=3)
    p3_info = p3_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p3_info.answer:
            return render(request, 'main/problem3.html', {'score': p3_info.score, 'flag': p3_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p3_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p3_info.score))

            user = Score.objects.filter(user=request.user)
            if user:
                instance = user[0]
            else:
                instance = Score.objects.create(user=request.user)
            instance.problem.add(Problem.objects.get(num=3))
            problems = instance.problem.all()
            my_score = 0
            for p in problems:
                my_score += p.score
            print(my_score)

            return HttpResponseRedirect('/main/problem3')
        else:
            return render(request, 'main/problem3.html', {'score': p3_info.score, 'flag': "오답입니다", 'username': request.user})

    return render(request, 'main/problem3.html', {'score': p3_info.score, 'username': request.user})


def problem4(request):
    p4_info = Problem.objects.filter(num=4)
    p4_info = p4_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p4_info.answer:
            return render(request, 'main/problem4.html', {'score': p4_info.score, 'flag': p4_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p4_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p4_info.score))

            user = Score.objects.filter(user=request.user)
            if user:
                instance = user[0]
            else:
                instance = Score.objects.create(user=request.user)
            instance.problem.add(Problem.objects.get(num=4))
            problems = instance.problem.all()
            my_score = 0
            for p in problems:
                my_score += p.score
            print(my_score)
            return HttpResponseRedirect('/main/problem4')
        else:
            return render(request, 'main/problem4.html', {'score': p4_info.score, 'flag': "오답입니다", 'username': request.user})

    return render(request, 'main/problem4.html', {'score': p4_info.score, 'username': request.user})


def problem5(request):
    p5_info = Problem.objects.filter(num=5)
    p5_info = p5_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p5_info.answer:
            return render(request, 'main/problem4.html', {'score': p5_info.score, 'flag': p5_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p5_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p5_info.score))

            user = Score.objects.filter(user=request.user)
            if user:
                instance = user[0]
            else:
                instance = Score.objects.create(user=request.user)
            instance.problem.add(Problem.objects.get(num=5))
            problems = instance.problem.all()
            my_score = 0
            for p in problems:
                my_score += p.score
            print(my_score)
            return HttpResponseRedirect('/main/problem5')
        else:
            return render(request, 'main/problem5.html', {'score': p5_info.score, 'flag': "오답입니다", 'username': request.user})

    return render(request, 'main/problem5.html', {'score': p5_info.score, 'username': request.user})


def problem6(request):
    p6_info = Problem.objects.filter(num=6)
    p6_info = p6_info[0]
    if request.method == 'POST':
        if request.POST.get('answer') and request.POST['answer'] == p6_info.answer:
            return render(request, 'main/problem6.html', {'score': p6_info.score, 'flag': p6_info.flag})
        elif request.POST.get('flag') and request.POST['flag'] == p6_info.flag:
            messages.success(
                request, 'Congratulations!! You got point +' + str(p6_info.score))

            user = Score.objects.filter(user=request.user)
            if user:
                instance = user[0]
            else:
                instance = Score.objects.create(user=request.user)
            instance.problem.add(Problem.objects.get(num=6))
            problems = instance.problem.all()
            my_score = 0
            for p in problems:
                my_score += p.score
            return HttpResponseRedirect('/main/problem6')
        else:
            return render(request, 'main/problem6.html', {'score': p6_info.score, 'flag': "오답입니다", 'username': request.user})

    return render(request, 'main/problem6.html', {'score': p6_info.score, 'username': request.user})
