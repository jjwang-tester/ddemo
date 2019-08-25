from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http.response import HttpResponse

class Adbs(View):

    def get(self,request):
        return HttpResponse("ORM")