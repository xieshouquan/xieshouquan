from django.test import TestCase
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'One_project.settings')
django.setup()
from hypermarket.models import Cmmodity


# Create your tests here.
cmmodity_list = Cmmodity.objects.filter(cmmoditytype=47)
# paginator = Paginator(cmmodity_list, 8)
# page = request.GET.get('page')
# contacts = paginator.get_page(page)
# data=[]
# for obj in cmmodity_list:
#     data_dict=obj.__dict__
#     data_dict['cmmoditytype']=obj.cmmoditytype.cmmodityname
#     del data_dict['cmmoditytype_id']
#     del data_dict['_state']
#     print(data_dict)

# data_list=list(cmmodity_list.values())
cmmoditymessage = Cmmodity.objects.filter(cmmodityid=1)
for obj in cmmoditymessage:
    cmmodity=obj.__dict__
    cmmodityspecs1=obj.cmmodityspecs1.split('，')
    cmmodityspecs2=obj.cmmodityspecs2.split('，')
    cmmodity['cmmodityspecs1']=cmmodityspecs1
    cmmodity['cmmodityspecs2']=cmmodityspecs2
    del cmmodity['_state']
print(cmmodity)
# cmmodityspecs2 = cmmoditymessage.cmmodityspecs2.split('，')
# print(111)
# print(type(cmmoditymessage))
# cmmoditymessage['cmmodityspecs1'] = cmmodityspecs1
# cmmoditymessage['cmmodityspecs2'] = cmmodityspecs2
# print(cmmoditymessage)