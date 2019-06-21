from django.urls import path, re_path

from polls.views import get_login, Login, get_cache_code
from . import views

urlpatterns=[
    path('get_login/',get_login,name='get_login'),
    path('login/',Login.as_view(),name='login'),
    re_path(r'get_cache_code/$',get_cache_code,name='cachecode')
]