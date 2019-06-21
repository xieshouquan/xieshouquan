from django.urls import path,re_path
from polls.views import login,Login,Myforms

urlpatterns = [
    path('login/',login,name='login'),
    path('Login/',Login.as_view(),name='Login'),
    re_path(r'Myforms/$',Myforms.as_view(),name='Myforms')
]