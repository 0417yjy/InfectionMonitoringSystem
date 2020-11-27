#from django.db import models
#from django.conf import settings
from .models import AbstractRegion, RegionLarge, RegionMedium


def make_medium_region(added_name, parent):
    added = RegionMedium(
        name=added_name,
        no_infected=0,
        no_deceased=0,
        no_offisolated=0,
        updated_time="2020-11-12T15:12:43Z",
        parent_region=parent
    )
    added.save()

north_cc = RegionLarge.objects.get(name="충청북도")
north_cc_added = ["청주시", "충주시", "제천시", "보은군", "옥천군", "영동군", "증평군", "진천군", "괴산군", "음성군", "단양군"]
south_cc = RegionLarge.objects.get(name="충청남도")
south_cc_added = ["천안시", "공주시", "보령시", "아산시", "서산시", "논산시", "계룡시", "당진시", "금산군", "부여군", "서천군", "청양군", "홍성군", "에산군", "태안군"]
north_jl = RegionLarge.objects.get(name="전라북도")
north_jl_added = ["전주시", "군산시", "익산시", "정읍시", "남원시", "김제시", "완주군", "진안군", "무주군", "장수군", "임실군", "순창군", "고창군", "부안군"]
south_jl = RegionLarge.objects.get(name="전라남도")
south_jl_added = ["목포시", "여수시", "순천시", "나주시", "광양시", "담양군", "곡성군", "구례군", "고흥군", "보성군", "화순군", "장흥군", "강진군", "해남군", "영암군", "무안군", "함평군", "영관군", "장성군", "완도군", "진도군", "신안군"]
north_ks = RegionLarge.objects.get(name="경상북도")
north_ks_added = ["포항시", "경주시", "김천시", "안동시", "구미시", "영주시", "영천시", "상주시", "문경시", "경산시", "군위군", "의성군", "청송군", "영양군", "영덕군", "청도군", "고령군", "성주군" ,"칠곡군", "에천군", "봉화군", "울진군", "울릉군"]
south_ks = RegionLarge.objects.get(name="경상남도")
south_ks_added = ["창원시", "진주시", "통영시", "사천시", "김해시", "밀양시", "거제시", "양산시", "의령군", "함안군", "창녕군", "고성군", "남해군", "하동군", "산청군", "함양군", "거창군", "합천군"]
jeju = RegionLarge.objects.get(name="제주특별자치도")
jeju_added = ["제주시", "서귀포시"]


def call(region_list, parent):
    for i in region_list:
        make_medium_region(i, parent)