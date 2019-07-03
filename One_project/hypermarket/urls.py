from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

from django.conf import settings
from hypermarket.views import cmmoditymess, index_check, test2, check

urlpatterns = [
    re_path(r'^index_check/$',index_check,name='index_check'),
    re_path(r'^cmmoditymess/$',cmmoditymess,name='cmmoditymess'),
    re_path(r'^check/$',check,name='check'),
    re_path(r'^test2/$',test2,name='test2'),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)