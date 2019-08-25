from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class GetTemplates(View):


    def get(self,request):
        content = {
            'name':'老王',
            'age':55,
            'wife':'美丽',
            'son':[
                '小李',
                '小王',
                '小刘',
            ],
            'msg':'架构师就是我'
        }
        return render(request, 'djangoindex.html',context=content)
