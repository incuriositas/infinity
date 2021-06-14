from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('score/', views.score, name='score'),
    # path('problem/', views.problem, name='problem'),
    path('problem1/', views.problem1, name='problem1'),
    path('problem2/', views.problem2, name='problem2'),
    path('problem3/', views.problem3, name='problem3'),
    path('problem4/', views.problem4, name='problem4'),
    path('problem5/', views.problem5, name='problem5'),
]
