from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from hypermarket.models import Cmmodity


def index(request):
    cmmodity_list = Cmmodity.objects.filter(cmmoditytype=47)
    paginator = Paginator(cmmodity_list, 8)
    page=request.GET.get('page')
    contacts=paginator.get_page(page)
    return render(request,'hypermarket/index.html',{'contacts':contacts})

