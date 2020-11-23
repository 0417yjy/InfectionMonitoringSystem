from django.shortcuts import render
from django.http import HttpResponse

from . import keyword 
from .models import StatisticValues
from datetime import datetime

def index(request):
    #통계 받아오는 API로 가져옴
    result = keyword.keywordFindAPI() 
    print(result)
     #context는 html에 data로 넘겨주는 parameter들을 담는것. 각각의 값을 전달한다
     #예를 들어 context에 result, result2, result3 이렇게 넣어서 전달하면
     #index.html에서 result, result2, result3 변수를 html 태그나 javascript코드 등에서 사용 가능하다.
    
    '''
    statisticDB = StatisticValues.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    statisticDBValues = list(StatisticValues.objects.all().values())
    context ={
        'result' : result,
        'statisticDBValues' : statisticDBValues,
    }
    print(statisticDBValues)
    '''
    # API 데이터를 DB 테이블 StatisticValues에 저장.
    try :
        #statisticValue = StatisticValues(updateTime = request.POST['updateTime'], TotalCase = request.POST['TotalCase'], 
        #                     TotalDeath = request.POST['TotalDeath'], TotalRecovered = request.POST['TotalRecovered'],
        #                     NowCase = request.POST['NowCase'], TotalChecking = request.POST['TotalChecking'],
        #                     notcaseCount = request.POST['notcaseCount'])
        
        YEAR= datetime.today().year        # 현재 연도 가져오기
        #print(YEAR)
        MONTH= datetime.today().month      # 현재 월 가져오기
        #print(MONTH)
        DAY= datetime.today().day        # 현재 일 가져오기
        #print(DAY)
        TodayDate=str(YEAR)+"."+str(MONTH)+"."+str(DAY)
        print(TodayDate)
        # if statisticDB.objects.get(updateTime=TodayDate).updateTime != TodayDate:
        #if not statisticDB.objects.filter(updateTime=TodayDate).exists(): 
        statisticValue = StatisticValues(updateTime = str(YEAR)+"."+result['updateTime'][23:28], 
                             TotalCase = result['TotalCase'], 
                             TotalDeath = result['TotalDeath'], TotalRecovered = result['TotalRecovered'],
                             NowCase = result['NowCase'], TotalChecking = result['TotalChecking'],
                             TodayCase = result['data0_1'], TodayRecovered =result['TodayRecovered'])
        statisticValue.save()
        
    except :
        statisticValue  = None
    # updateTime # 정보 업데이트 시간 data['updateTime'][23:28] -> 월.일(00.00 구조)

    statisticDB = StatisticValues.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    statisticDBValues = list(StatisticValues.objects.all().values())
    context ={
        'result' : result,
        'statisticDBValues' : statisticDBValues,
    }
    print(statisticDBValues)
    print(statisticValue)
    return render(request, 'index.html', context)

def mapview(request):
    return render(request, 'map.html')

# Create your views here.

