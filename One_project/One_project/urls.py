"""One_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path,include

from hypermarket import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^consumer/',include(('consumer.urls','consumer'),namespace='consumer')),
    re_path(r'hypermarket/',include(('hypermarket.urls','hypermarket'),namespace='hypermarket'))
]
