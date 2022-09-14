import json
import random

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from trident.decorators import test_decorator
from users.models import UserProfile
from django.contrib.auth.models import User
from trident.forms import SignupForm

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/index.html')


@test_decorator
def home(request):
    return render(request, 'base/base.html')


def signup(request):
    form = SignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def login(request):
    data = []
    context = {'data': data}
    return render(request, 'login.html', context)


def save(request):
    response = {}
    form = SignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            userData = User()
            userData.first_name = request.POST["name"]
            userData.username = "TRIDENT" + request.POST["name"].upper() + str(random.randint(0, 99))
            userData.email = request.POST["email"]
            userData.is_staff = 1
            userData.set_password(request.POST["password"])
            userData.save()
            inserted = User.objects.latest('id')
            profile = UserProfile()
            profile.user_id = inserted.id
            profile.user_address = request.POST['address']
            profile.user_phone = request.POST['phone']
            if inserted is not None:
                profile.save()
                response['flag'] = 1
                response['msg'] = "Successfully added"
                response['data'] = None
            else:
                response['flag'] = 0
                response['msg'] = "Failed..! Something went wrong"
                response['data'] = None
        else:
            response['flag'] = 2
            response['msg'] = "Fill all the Fields"
            response['data'] = None
    else:
        response['flag'] = 2
        response['msg'] = "Failed..! Something went wrong"
        response['data'] = None
    return HttpResponse(json.dumps(response))


def auth(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('dashboard')
        else:
            print('is not logged in')
            messages.error(request, "Invalid username or password.")
            return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('login')
