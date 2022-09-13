from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from trident.decorators import test_decorator
from users.models import Users
from django.contrib.auth import authenticate, login as auth_login


def dashboard(request):
    return render(request, 'base/dashbase.html')


@test_decorator
def home(request):
    return render(request, 'base/base.html')


def signup(request):
    data = []
    context = {'data': data}
    return render(request, 'signup.html', context)


def login(request):
    data = []
    context = {'data': data}
    return render(request, 'login.html', context)


def save(request):
    if request.method == "POST":
        userData = Users()
        userData.first_name = request.POST["name"]
        userData.email = request.POST["email"]
        userData.is_staff = 1
        userData.set_password(request.POST["password"])
        userData.address = request.POST['address']
        userData.phone = request.POST['phone']
        res = userData.save()
        print(res)

    else:
        pass
    return redirect("/")


def auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, f"You are now logged in as {email}")
            return redirect('/')
        else:
            print('is not logged in')
            messages.error(request, "Invalid username or password.")
            return redirect('/')
