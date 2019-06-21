"""django619 URL Configuration

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
from django.urls import path,re_path,include
from polls.views import login

urlpatterns = [
    path('',login,name='login'),
    re_path(r'^mis_task/',include(('mis_task.urls','mis_task'),namespace='get_mis_task')),
    re_path(r'^polls/',include(('polls.urls','polls'),namespace='get_polls')),
]
