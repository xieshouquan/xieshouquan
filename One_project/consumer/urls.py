from django.urls import re_path
from consumer.views import login, Register, message_center, get_code

urlpatterns = [
    re_path(r'^get_code/$', get_code, name='getcode'),
    re_path(r'^login/$',login,name='login'),
    re_path(r'^Register/$',Register.as_view(),name='Register'),
    re_path(r'^message_center/$',message_center,name='message_center'),
]
