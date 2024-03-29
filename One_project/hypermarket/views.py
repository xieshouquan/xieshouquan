import json
from datetime import datetime, date
from decimal import Decimal

from django.core import serializers
from django.core.paginator import Paginator

from django.db.models import QuerySet
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from consumer.models import UserPin
from hypermarket.models import Cmmodity, CmmodityType

# 主页
def index(request):
    cmmodity_list = Cmmodity.objects.filter(cmmoditytype=47)
    paginator = Paginator(cmmodity_list, 8)
    page=request.GET.get('page')
    contacts=paginator.get_page(page)
    return render(request,'hypermarket/index.html',{'contacts':contacts})

# 商品详情页请求与加载
def cmmoditymess(request):
    id=request.GET.get('id')
    pinlun = UserPin.objects.filter(cmmodityid_id=id)
    cmmodity = Cmmodity.objects.get(cmmodityid=id)
    cmmodityspecs1=cmmodity.cmmodityspecs1.split('，')
    cmmodityspecs2 = cmmodity.cmmodityspecs2.split('，')
    return render(request,'hypermarket/cmmoditymess.html',{'cmmodity':cmmodity,'cmmodityspecs1':cmmodityspecs1,'cmmodityspecs2':cmmodityspecs2,'pinlun':pinlun})

# 编码方法
class MyEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, datetime):

            return obj.__str__()

        elif isinstance(obj, Decimal):

            return obj.__str__()

        elif isinstance(obj, date):

            return obj.__str__()

        elif isinstance(obj, QuerySet):

            return list(obj)

        else:

            return json.JSONEncoder.default(self, obj)

# 主页异步加载请求
def index_check(request):
    num = request.GET.get('number')
    cmmodity_list_mess=[]
    cmmodity_list = Cmmodity.objects.filter(cmmoditytype=num)
    for obj in cmmodity_list:
        data_dict = obj.__dict__
        data_dict['cmmoditytype'] = obj.cmmoditytype.cmmodityname
        del data_dict['cmmoditytype_id']
        del data_dict['_state']
        cmmodity_list_mess.append(data_dict)
        print(data_dict)
    return JsonResponse({'data':cmmodity_list_mess},encoder=MyEncoder)

def test2(request):
    return render(request,'public/test.html')

# 查询请求
def check(request):
    name=request.GET.get('name')
    print(name)
    cmmodity_list = Cmmodity.objects.filter(cmmoditytype__cmmodityname='name')
    paginator = Paginator(cmmodity_list, 12)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    print(contacts)
    return render(request, 'hypermarket/check.html', {'contacts': contacts,'name':name})











