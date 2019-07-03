from django.urls import re_path
from consumer.views import login, Register, message_center, get_code, Login, personal_center, shop_car, save_cmmodity, \
    dingdan, buy, enevaluation, save_pinglun, save_info, logoutuser

urlpatterns = [
    re_path(r'^get_code/$', get_code, name='getcode'),
    re_path(r'^login/$',login,name='login'),
    re_path(r'^Register/$',Register.as_view(),name='Register'),
    re_path(r'^Login/$',Login,name='Login'),
    re_path(r'^message_center/$',message_center,name='message_center'),
    re_path(r'^personal_center/$',personal_center,name='personal_center'),
    re_path(r'^shop_car/$',shop_car,name='shop_car'),
    re_path(r'^save_cmmodity/$',save_cmmodity,name='save_cmmodity'),
    re_path(r'^dingdan/$',dingdan,name='dingdan'),
    re_path(r'^buy/$',buy,name='buy'),
    re_path(r'^enevaluation/$',enevaluation,name='enevaluation'),
    re_path(r'^save_pinglun/$',save_pinglun,name='save_pinglun'),
    re_path(r'^save_info/$',save_info,name='save_info'),
    re_path(r'^logoutuser/$',logoutuser,name='logoutuser'),
]
