from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import View
from django.utils.decorators import method_decorator

# Create your views here.

def login_view_decorator_self(fn):
    def warpper(request, *args, **kwargs):
        print(request.method)
        print(request.path)
        return fn(request, *args, **kwargs)
    return warpper

@method_decorator(login_view_decorator_self,name="dispatch")
class LoginView(View):
    def get(self, request):
        return HttpResponse('类视图---GET---登录页面！')

    def post(self, request):
        return HttpResponse('类视图---POST---登录请求！')
