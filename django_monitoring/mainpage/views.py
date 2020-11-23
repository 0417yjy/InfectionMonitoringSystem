from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber
def index(request):
    return render(request, 'index.html')

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
# Create your views here.
