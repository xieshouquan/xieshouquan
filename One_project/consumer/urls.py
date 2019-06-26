from django.urls import re_path
from consumer.views import login, Register, message_center, get_code, Login, personal_center

urlpatterns = [
    re_path(r'^get_code/$', get_code, name='getcode'),
    re_path(r'^login/$',login,name='login'),
    re_path(r'^Register/$',Register.as_view(),name='Register'),
    re_path(r'^Login/$',Login,name='Login'),
    re_path(r'^message_center/$',message_center,name='message_center'),
    re_path(r'^personal_center/$',personal_center,name='personal_center'),
]
