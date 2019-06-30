import json
from datetime import datetime, date
from decimal import Decimal

from django.core import serializers
from django.core.paginator import Paginator

from django.db.models import QuerySet
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from hypermarket.models import Cmmodity


def index(request):
    cmmodity_list = Cmmodity.objects.filter(cmmoditytype=47)
    paginator = Paginator(cmmodity_list, 8)
    page=request.GET.get('page')
    contacts=paginator.get_page(page)
    return render(request,'hypermarket/index.html',{'contacts':contacts})

def cmmoditymess(request):
    id=request.GET.get('id')
    cmmodity = Cmmodity.objects.get(cmmodityid=id)
    cmmodityspecs1=cmmodity.cmmodityspecs1.split('，')
    cmmodityspecs2 = cmmodity.cmmodityspecs2.split('，')
    return render(request,'hypermarket/cmmoditymess.html',{'cmmodity':cmmodity,'cmmodityspecs1':cmmodityspecs1,'cmmodityspecs2':cmmodityspecs2})


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













