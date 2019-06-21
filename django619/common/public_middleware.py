from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class MyAuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        #获取请求
        no_auth_request=[]
        if (request.path in no_auth_request)==False:
            if (request.user.is_authenticated and request.user.is_active and request.user.is_staff)==False:
                print('未登录')
                return redirect('/')
    def process_response(self,request,response):
        #响应数据
        print('response')
        return response
    def process_exception(self,request,exception):
        #异常处理
        print('exception')