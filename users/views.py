from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import *


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def login(request):
    if request.POST:
        username = ''
        password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
    ctx = {}
    return render(request, 'user/login.html', ctx)


def logout(request):
    logout(request)
    return redirect('/')


@login_required
def user_only(request):
    return HttpResponse("<p>this message is for logged in user only.</p>")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
        return redirect('/')
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        return render(request, "user/register.html", ctx)
