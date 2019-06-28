from django.urls import re_path
from hypermarket.views import cmmoditymess,index_check,test2
urlpatterns = [

    re_path(r'^index_check/$',index_check,name='index_check'),
    re_path(r'^cmmoditymess/$',cmmoditymess,name='cmmoditymess'),
    re_path(r'^test2/$',test2,name='test2'),
]