#-*- coding:utf-8 -*-
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen , Request
from . import * #if using on django , should using .apikey instead apikey 
import json


import requests
import re #계산을 위한 특수문자 제거

key = 'f14954c4a0b04d9a53b1603e20d40e1b8'  #API 키(https://api.corona-19.kr/ 에서 무료 발급 가능)

def keywordFindAPI():
    #####
    korea = "http://api.corona-19.kr/korea?serviceKey="
    country = "http://api.corona-19.kr/korea/country?serviceKey="
    countryNew='https://api.corona-19.kr/korea/country/new/?serviceKey='

    key = 'f14954c4a0b04d9a53b1603e20d40e1b8' #API 키(https://api.corona-19.kr/ 에서 무료 발급 가능)
    ###
    print('서버에 데이터를 요청하고 있습니다.. \n\n')

    response = requests.get(korea + key)
    text = response.text
    data = json.loads(text)

    response2 = requests.get(country + key)
    text2 = response2.text
    data2 = json.loads(text2)

    responseNew = requests.get(countryNew + key)
    textNew = responseNew.text
    dataNew = json.loads(textNew)

    #####
    code = response.status_code
    code2 = response2.status_code

    data.update(data2)
    data.update(dataNew)
    # print(dataNew)
    return data 

def getKoreaData():
    #####
    korea = "http://api.corona-19.kr/korea?serviceKey="

    ###
    print('국내 데이터 가져오는 중.. \n\n')

    response = requests.get(korea + key)
    text = response.text
    data = json.loads(text)

    #####
    #code = response.status_code
    return data 

def getCountryData():
    #####
    countryNew = 'https://api.corona-19.kr/korea/country/new/?serviceKey='
    
    ###
    print('시도별 발생동향 가져오는 중.. \n\n')

    responseNew = requests.get(countryNew + key)
    textNew = responseNew.text
    dataNew = json.loads(textNew)

    #####
    #code = responseNew.status_code

    return dataNew