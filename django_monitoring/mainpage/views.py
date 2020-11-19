from django.shortcuts import render
from django.http import HttpResponse

from . import keyword 

def index(request):
    #통계 받아오는 API로 가져옴
    result = keyword.keywordFindAPI() 
    #print(result)
     #context는 html에 data로 넘겨주는 parameter들을 담는것. 각각의 값을 전달한다
     #예를 들어 context에 result, result2, result3 이렇게 넣어서 전달하면
     #index.html에서 result, result2, result3 변수를 html 태그나 javascript코드 등에서 사용 가능하다.
    context ={
        'result' : result
    }
    
    return render(request, 'index.html')

def mapview(request):
    return render(request, 'map.html')

# Create your views here.

