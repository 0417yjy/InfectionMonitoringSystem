from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import StatisticValues, RegionLarge, RegionMedium, Subscriber
from . import keyword
from datetime import datetime
from .mailsender import send_safe_mail

def convert_to_int_with_comma(str_num):
    return int(str_num.replace(',', ''))

def send_messages(large_obj, increased):
    region_name = large_obj.name

    # 중분류가 '전체선택'인 구독자들에 한하여 메시지 전송
    medium_all_select_obj = RegionMedium.objects.get(name='전체선택')
    subscribers = Subscriber.objects.filter(large_region=large_obj).filter(medium_region=medium_all_select_obj)
    
    # 이메일 구독자들
    email_subs = subscribers.filter(sub_type='Email')
    emails = email_subs.values_list('address', flat=True)
    send_safe_mail(emails, region_name, increased)

@receiver(post_save, sender=StatisticValues)
def StatisticValues_post_save(sender, **kwargs):
    if kwargs['created']:
        result = keyword.getCountryData()

        for region in result:
            if region != 'resultCode' and region != 'resultMessage':
                increased_num = 0

                if region == 'korea':
                    # 대분류가 '전체선택' 인 경우
                    region_name = result[region]['countryName']
                    region_obj = RegionLarge.objects.get(name='전체선택')
                else:
                    # 그 외 나머지 지역들
                    region_name = result[region]['countryName']
                    region_obj = RegionLarge.objects.filter(name__contains=region_name[0]).get(name__contains=region_name[1])

                    # 늘어난 확진자 수 계산
                    increased_num = convert_to_int_with_comma(result[region]['totalCase']) - region_obj.no_infected

                    region_obj.no_infected = convert_to_int_with_comma(result[region]['totalCase'])
                    region_obj.no_deceased = convert_to_int_with_comma(result[region]['death'])
                    region_obj.no_offisolated = convert_to_int_with_comma(result[region]['recovered'])
                    region_obj.updated_time = datetime.now()
                    region_obj.save()

                    if increased_num > 0:
                        send_messages(region_obj, increased_num)
        print('Updated RegionLarge instances')