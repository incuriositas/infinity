from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                # email=request.POST['email'],
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'user/regiter.html')
    return render(request, 'user/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main/index')
            # return render(request, 'main/index.html', {'username': username})
        else:
            return render(request, 'user/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'user/login.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('/')
