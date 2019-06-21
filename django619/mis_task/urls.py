from django.urls import path
from mis_task.views import get_xiaoque,Mis_taskq,check

urlpatterns = [
    path('get_xiaoque/',get_xiaoque,name='xiaoque'),
    path('ti_mis_task/',Mis_taskq.as_view(),name='ti_mis_task'),
    path('check/',check,name='check')
]