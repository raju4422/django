from django.http import HttpResponse
from django.shortcuts import render,redirect

def dashboard(request):
    return render(request,'base/dashbase.html')

def home(request):
    return render(request,'base/base.html')

def signup(request):
    data = []
    context = {'data':data}
    return render(request,'signup.html',context)

def login(request):
    data = []
    context = {'data':data}
    return render(request,'login.html',context)

