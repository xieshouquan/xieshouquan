import random

from django.contrib import auth
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from consumer.cache_img import get_cache_code_info
from consumer.forms import RegForm, UserForm
from consumer.models import MyUser, UserCmmodity
from hypermarket.models import Cmmodity



def message_center(request):
    return render(request, 'consumer/message_center.html')


# 验证码
def get_code(request):
    img, code = get_cache_code_info()
    request.session['code'] = code
    return HttpResponse(img.getvalue(), content_type='image/png')

#个人资料
def personal_center(request):
    user = MyUser.objects.get(id=18)
    return render(request,'consumer/personal_center.html',{"userinfo":user})

#登录加载
def login(request):
    return render(request, 'consumer/login.html')

class Register(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'consumer/register.html')
    def post(self, request, *args, **kwargs):
        form = RegForm(request.POST, request.FILES)
        code = request.POST.get('cache_code', None)
        if code == request.session['code']:
            if form.is_valid():
                password1 = form.cleaned_data['userPassword1']
                password2 = form.cleaned_data['userPassword2']
                if password1 == password2:
                    form_file = MyUser(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['userPassword1'],
                        userphone=form.cleaned_data['userphone'],
                        userEmail=form.cleaned_data['userEmail']
                    )
                    form_file.set_password(form_file.password)
                    form_file.save()
                    return JsonResponse({'msg':'注册成功','status':'success'})
                else:
                    return JsonResponse({'status': 'fail_one', 'msg': '密码输入不一致'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '输入有误'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '验证码错误'})

# 登陆
def Login(request):
    forms = UserForm(request.POST,request.FILES)
    if forms.is_valid():
        user = auth.authenticate(username=forms.cleaned_data['username'],password=forms.cleaned_data['password'])
        if user:
            auth.login(request,user)
            return JsonResponse({'msg':'登录成功','status':'success'})
        else:
            return JsonResponse({'msg':'用户名或者密码错误','status':'fail'})
    else:
        form_error = forms.errors.as_json()
        return JsonResponse({'msg':'格式不正确','data':form_error,'status':'form_error'})

def save_cmmodity(request):
    id=request.GET.get('id')
    number=request.GET.get('number')
    type1=request.GET.get('type1')
    type2=request.GET.get('type2')
    name=request.GET.get('name')
    cmmodity=UserCmmodity(cmmodityname=name,type1=type1,type2=type2,pay_number=number,cmmoditynumber=random.randint(10000000,99999999))
    cmmodity.pay_id_id=id
    cmmodity.pay_userid_id=1
    cmmodity.save()
    return JsonResponse({'reslut':'success'})

def shop_car(request):
    cmmodity=UserCmmodity.objects.filter(pay_userid_id=1,pay_state=False)
    paginator = Paginator(cmmodity, 8)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request,'consumer/shop_car.html',{'contacts':contacts})

def dingdan(request):
    cmmodity = UserCmmodity.objects.filter(pay_userid_id=1,pay_state=True)
    paginator = Paginator(cmmodity, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request,'consumer/dingdan.html',{'contacts':contacts})

def buy(request):
    price=request.GET.get('price')
    number=request.GET.get('number')
    address=request.GET.get('address')
    bianhao=request.GET.get('bianhao')
    UserCmmodity.objects.filter(cmmoditynumber=bianhao).update(price=price,pay_number=number,address=address,pay_state=True)
    return JsonResponse({'state':'success'})



















