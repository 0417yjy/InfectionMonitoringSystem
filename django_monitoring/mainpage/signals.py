from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import StatisticValues, RegionLarge
from . import keyword
from datetime import datetime

def convert_to_int_with_comma(str_num):
    return int(str_num.replace(',', ''))

@receiver(post_save, sender=StatisticValues)
def StatisticValues_post_save(sender, **kwargs):
    if kwargs['created']:
        result = keyword.getCountryData()
        is_increased = False # 해당 지역에서 확진자가 늘었는지 여부

        for region in result:
            if region != 'resultCode' and region != 'resultMessage' and region != 'korea':
                # 전체선택 부분
                if region == 'korea':
                    region_name = result[region]['countryName']
                    region_obj = RegionLarge.objects.get(name='전체선택')

                    if region_obj.no_infected < convert_to_int_with_comma(result[region]['totalCase']):
                        # 새로 늘었으면 is_increased를 True로 변환함 -> 메시지 전송 플래그
                        is_increased = True
                        region_obj.no_infected = convert_to_int_with_comma(result[region]['totalCase'])
                    region_obj.no_deceased = convert_to_int_with_comma(result[region]['death'])
                    region_obj.no_offisolated = convert_to_int_with_comma(result[region]['recovered'])
                    region_obj.updated_time = datetime.now()
                    region_obj.save()
                # 그 외 나머지 지역들
                else:
                    region_name = result[region]['countryName']
                    region_obj = RegionLarge.objects.filter(name__contains=region_name[0]).get(name__contains=region_name[1])

                    if region_obj.no_infected < convert_to_int_with_comma(result[region]['totalCase']):
                        # 새로 늘었으면 is_increased를 True로 변환함 -> 메시지 전송 플래그
                        is_increased = True
                        region_obj.no_infected = convert_to_int_with_comma(result[region]['totalCase'])
                    region_obj.no_deceased = convert_to_int_with_comma(result[region]['death'])
                    region_obj.no_offisolated = convert_to_int_with_comma(result[region]['recovered'])
                    region_obj.updated_time = datetime.today()
                    region_obj.save()
        print('Updated RegionLarge instances')