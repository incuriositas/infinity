from django.db import models
from django.contrib.auth.models import User
from main.models import Problem


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ManyToManyField(Problem, related_name='solved')
