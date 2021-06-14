from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Score
from django.contrib.auth.models import User


def score(request):
    user = request.user
    instance = Score.objects.get(user=user)
    problems = instance.problem.all()

    my_score = 0
    for p in problems:
        my_score += p.score

    users = User.objects.all()
    board = []
    for i in users:
        try:
            s = Score.objects.get(user=i)
            p = s.problem.all()
            g = 0
            for q in p:
                g += q.score
            board.append([i, g])
        except:
            continue

    return render(request, 'score/tables.html', {'username': user, 'score': my_score, 'board': board})
