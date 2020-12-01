from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from . import keyword 
from .models import StatisticValues, RegionLarge, RegionMedium, Subscriber
from .forms import SubscirberForm
from datetime import datetime
from . import LocationInfo
import json

def index(request):
    #============================================ Start of 'contents-home.html' ====================================================
    #통계 받아오는 API로 가져옴
    result = keyword.keywordFindAPI()
    #print(result)
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
        # #print(YEAR)
        # MONTH= datetime.today().month      # 현재 월 가져오기
        # #print(MONTH)
        # DAY= datetime.today().day        # 현재 일 가져오기
        #print(DAY)
        #TodayDate=str(YEAR)+"."+str(MONTH)+"."+str(DAY)
        #print(TodayDate)
        # if statisticDB.objects.get(updateTime=TodayDate).updateTime != TodayDate:
        #if not statisticDB.objects.filter(updateTime=TodayDate).exists(): 
        statisticValue = StatisticValues(updateTime = str(YEAR)+"."+result['updateTime'][23:28], 
                             TotalCase = result['TotalCase'], 
                             TotalDeath = result['TotalDeath'], TotalRecovered = result['TotalRecovered'],
                             NowCase = result['NowCase'], TotalChecking = result['TotalChecking'],
                             TodayCase = result['data0_1'], TodayRecovered =result['TodayRecovered'])
        statisticValue.save()
        
    except Exception as e:
        print(e)
        statisticValue  = None
    # updateTime # 정보 업데이트 시간 data['updateTime'][23:28] -> 월.일(00.00 구조)

    statisticDB = StatisticValues.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    statisticDBValues = list(StatisticValues.objects.all().values())
    
    #print(statisticDBValues)
    #print(statisticValue)
    #=============================================== End of 'contents-home.html' ========================================================


    #============================================ Start of 'contents-subscribe.html' ====================================================
    largeRegions = RegionLarge.objects.all()
    largeRegionsValues = serializers.serialize('json', largeRegions)
    mediumRegions = RegionMedium.objects.all()
    mediumRegionsValues = serializers.serialize('json', mediumRegions)
    #============================================= End of 'contents-subscribe.html' =====================================================
    #============================================= Start of 'content-mapview.html' ======================================================
    locationset = LocationInfo.get_location(result)
    seoul_gu_results = LocationInfo.scraping_data()
    #============================================= End of 'content-mapview.html' =============================== #=======================
    context = {
        # contents-home
        'result' : result,
        'statisticDBValues': statisticDBValues,
        # contents-subscribe
        'largeRegions': largeRegionsValues,
        'mediumRegions': mediumRegionsValues,
        # contents-mapview
        'locationset' : locationset,
        'seoul_gu_result' : seoul_gu_results,
    }
    return render(request, 'index.html', context)

def subscribe_email(request):
    if request.method == 'POST':
        form = SubscirberForm(request.POST)
        if form.is_valid():
            email = request.POST.get('address', 'false')
            #print(email)

            # 지역 구독 리스트 가져오기
            i = 0
            while request.POST.get('large_' + str(i)):
                large_pk = request.POST.get('large_' + str(i))
                med_pk = request.POST.get('med_' + str(i))
                print(str(i) + ': ' + large_pk + ', ' + med_pk)
                
                # 데이터베이스에 저장
                new_subscription = Subscriber(
                    address=email,
                    sub_type="Email",
                    large_region=RegionLarge.objects.get(pk=large_pk),
                    medium_region=RegionMedium.objects.get(pk=med_pk)
                )
                new_subscription.save()

                i += 1

            # 성공 메시지 전달    
            messages.success(request, str(i) + '개 지역이 ' + email + '의 구독 리스트에 추가되었습니다!')
            return redirect('index')
    else:
        form = SubscirberForm(request.POST)
    return redirect('index')

def subscribe_kakao(request):
    if request.method == 'POST':
        form = SubscirberForm(request.POST)
        if form.is_valid():
            kakao_id = request.POST.get('address', 'false')
            kakao_nickname = request.POST.get('nickname', 'false')
            #print(email)

            # 지역 구독 리스트 가져오기
            i = 0
            while request.POST.get('large_' + str(i)):
                large_pk = request.POST.get('large_' + str(i))
                med_pk = request.POST.get('med_' + str(i))
                #print(str(i) + ': ' + large_pk + ', ' + med_pk)
                
                # 데이터베이스에 저장
                new_subscription = Subscriber(
                    address=kakao_id,
                    sub_type="Kakao",
                    large_region=RegionLarge.objects.get(pk=large_pk),
                    medium_region=RegionMedium.objects.get(pk=med_pk)
                )
                new_subscription.save()

                i += 1

            # 성공 메시지 전달    
            messages.success(request, str(i) + '개 지역이 ' + kakao_nickname + '님의 구독 리스트에 추가되었습니다!')
            return redirect('index')
    else:
        form = SubscirberForm(request.POST)
    return redirect('index')    

def mapview(request):
    return render(request, 'map.html')

#구독을 위한 관심지역 설정을 위한 DB view 설정
#전체설정 안하면 뷰오류나서 나중에 DB구현한다음에
'''def index(request) :
    Subscriber = Subscriber.objects.all() # 테이블 데이타를 전부 가져오기 위한 메소드
    context = {'SubscribeData' : SubscribeData}
    try :
        Subscribedatas = SubscribeData(address = request.POST['address'], sub_type = request.POST['sub_type'],
                             large_region = request.POST['large_region'], medium_region = request.POST['medium_region'],
                             small_region = request.POST['small_region'])
        Subscirbedatas.save()
    except :
        Subscribedatas  = None
    return render(request, 'contents-subscribe.html', context) # render는 view에서 템플릿에 전달할 데이타를 Dictionary로 전달한다
'''