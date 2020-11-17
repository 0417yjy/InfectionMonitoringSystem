from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def mapview(request):
    return render(request, 'map.html')

# Create your views here.

from . import keyword # 이거 고쳐야 함.

# class FormView(generic.View): #formtest
    # template_name = 'mainpage/contents-statistics.html'

def statisticsView(self,request):
    template_name = 'contents-statistics.html'
    result = keyword.keywordFindAPI() #여기!
    context =list({
        'result' : result
    })
    return render(request, template_name, context)
