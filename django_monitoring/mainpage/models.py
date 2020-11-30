'''
File: models.py
Project: EDPS
File Created: Sunday, 8th November 2020 11:32:24 am
Author: Jongyeon Yoon (0417yjy@naver.com)
-----
Last Modified: Thursday, 12th November 2020 9:58:07 pm
Modified By: Jongyeon Yoon (0417yjy@naver.com>)
-----
Copyright 2020 Jongyeon Yoon
'''


from django.db import models
# from datetime import datetime 

# Create your models here.
class AbstractRegion(models.Model):  # Abstract class of region models
    name = models.CharField(max_length=16)
    no_infected = models.IntegerField() # 각 지역별로도 감염 통계를 저장함
    no_deceased = models.IntegerField()
    no_offisolated = models.IntegerField()
    updated_time = models.DateTimeField()
    
    class Meta:
        abstract = True

class RegionLarge(AbstractRegion):
    # 전체선택 / 특별시 / 광역시 / 도 / 해외유입
    def __str__(self):
        return self.name

class RegionMedium(AbstractRegion):
    # 전체선택 / 구 / 군 / 시
    parent_region = models.ForeignKey('RegionLarge', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# class RegionSmall(AbstractRegion):
#     # 전체선택 / 동 / 읍
#     parent_region = models.ForeignKey('RegionMedium', on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name

class Subscriber(models.Model):
    SUBSCRIBE_TYPE_CHOICES = models.TextChoices('SubscribeType','Email Kakao')

    address = models.CharField(max_length=20)  # kakaotalk id or email address
    sub_type = models.CharField(max_length=5, choices=SUBSCRIBE_TYPE_CHOICES.choices)

    # Has each region's id
    large_region = models.ForeignKey('RegionLarge', on_delete=models.CASCADE)
    medium_region = models.ForeignKey('RegionMedium', on_delete=models.CASCADE)
    #small_region = models.ForeignKey('RegionSmall', on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_type + ": " + self.address + ": " + str(self.large_region) + "/" + str(self.medium_region)

# class Facility(models.Model):
#     # Entity about facility (a kind of map overlay components)
#     FACILITY_TYPE_CHOICES = models.TextChoices('FacilityType', 'Hospital Pharmacy Convenience')

#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=100)
#     fac_type = models.CharField(max_length=12, choices=FACILITY_TYPE_CHOICES.choices)
#     #small_region = models.ForeignKey('RegionSmall', on_delete=models.CASCADE)

#     def __str__(self):
#         return small_region + ": " + self.name + ": " + self.fac_type

class Infected(models.Model):
    STATUS_CHOICES = models.TextChoices('StatusType','Infected Deceased Off-Isolated')

    name = models.CharField(max_length=30)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES.choices)

class InfectedMovement(models.Model):
    infected = models.ForeignKey('Infected', on_delete=models.CASCADE)
    #small_region = models.ForeignKey('RegionSmall', on_delete=models.CASCADE)
    medium_region = models.ForeignKey('RegionMedium', on_delete=models.CASCADE, default=1)
    moved_date = models.DateTimeField()
    exact_address = models.CharField(max_length=100) # 방문 장소의 주소
    desc = models.CharField(max_length=20)  # 방문 장소 이름
    
class StatisticValues(models.Model):
    # 지역별 감염 정보 외의, 전체 감염 정보 / 검사완료 & 검사중 등 다른 통계 자료를 저장하는 테이블
    # st_name = models.CharField(max_length=20)
    # value = models.IntegerField()
    # updated_time = models.DateTimeField()

    updateTime = models.CharField(max_length=15, default="2020.11.21", primary_key=True) # 정보 업데이트 시간 data['updateTime'][23:28] -> 월.일(00.00 구조)
    TotalCase = models.TextField(default="0")            # 총 확진자
    TotalDeath = models.TextField(default="0")           # 총 사망자
    TotalRecovered = models.TextField(default="0")       # 총 완치자
    NowCase = models.TextField(default="0")              # 치료중인 사람
    TotalChecking = models.TextField(default="0")        # 검사완료 
    # notcaseCount = models.TextField(default="0")         # 결과 음성

    TodayCase = models.TextField(default="0")            # 전일 대비 확진자, data2["data0_1"]의미 
    TodayRecovered = models.TextField(default="0")       # 전일 대비 완치자


    def __str__(self):
        return self.updateTime





# from django.db import models
# from mainpage.models import StatisticValues