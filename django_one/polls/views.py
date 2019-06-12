from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello , world')

def get_work01(request):
    return render(request,'work01.html',context={'data':'123456'})