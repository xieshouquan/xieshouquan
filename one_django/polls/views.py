
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View

from polls.cache_img import get_cache_code_info


def get_login(request):
    return render(request,'polls/login.html')

user='admin'
pasd='123456'

class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request,'polls/login.html')
    def post(self,request,*args,**kwargs):
        data=request.POST
        code=data.get('cache_code')
        username=data.get('username')
        password=data.get('pwd')
        if username==user and password==pasd:
            if code==request.session['code']:
                return render(request,'polls/manger.html')
            else:
                result='验证失败'
        else:
            result='用户名或密码错误'
        return HttpResponse(result)

def get_cache_code(request):
    img,code=get_cache_code_info()
    request.session['code']=code
    return HttpResponse(img.getvalue(),content_type='image/png')
