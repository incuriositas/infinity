from django.db import models

# Create your models here.


class Problem(models.Model):
    num = models.IntegerField()
    score = models.IntegerField()
    answer = models.CharField(max_length=200)
    flag = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
