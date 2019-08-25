from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import View

# Create your views here.



class LoginView(View):

    def get(self,request):

        return HttpResponse('类视图---GET---登录页面！')
    def post(self,request):

        return HttpResponse('类视图---POST---登录请求！')