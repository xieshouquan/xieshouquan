from django.shortcuts import render, redirect
from django.views import View

from polls.forms import LoginForm
from polls.models import User
from django.http import HttpResponse, JsonResponse


# Create your views here.
def login(request):
    return render(request,'polls/login.html')

class Myforms(View):
    def get(self,request,*args,**kwargs):
        forms=LoginForm()
        return render(request, 'polls/forms.html',{'form':forms})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            user=User.objects.filter(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user.count():
                return redirect('/')
        else:
            result=form.errors()
        return JsonResponse({'data':result})

class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request,'polls/login.html')
    def post(self,request,*args,**kwargs):
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user=User.objects.filter(username=username,password=password)
        if user:
            return render(request,'mis_task/xiaoque1.html')
        else:
            result='用户名或密码错误'
        return HttpResponse(result)