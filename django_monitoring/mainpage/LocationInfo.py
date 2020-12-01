from urllib.request import Request, urlopen
import requests, bs4, json
from bs4 import BeautifulSoup





def get_location(APIresult):
    apiresult = APIresult
    lat = []
    lng = []
    resultset = []
    headers = {"Authorization": "KakaoAK f65e7c08cbfe6221c3795ebb8da80931"} #지역검색 api
    for i in range(1,19):
        location_name = 'data'+str(i)+'_0'
        url = "https://dapi.kakao.com/v2/local/search/address.json?"
        if apiresult[location_name]=='광주':
            query = "query=광주광역시"
            url = url+query
            result = requests.get(url,headers = headers)
            search_inf = json.loads(result.text)
            lat.append(search_inf['documents'][0]['address']['y'])
            lng.append(search_inf['documents'][0]['address']['x'])
        elif apiresult[location_name]=='검역':
            lat.append('34.48321535036117')
            lng.append('129.36847815669026')
        elif apiresult[location_name]=='서울':
            query = "query=서울특별시"
            url = url+query
            result = requests.get(url,headers = headers)
            search_inf = json.loads(result.text)
            lat.append(search_inf['documents'][0]['address']['y'])
            lng.append(search_inf['documents'][0]['address']['x'])
        else:
            print(apiresult[location_name])
            query = "query="+apiresult[location_name]
            print(query)
            url = url+query
            result = requests.get(url,headers = headers)
            search_inf = json.loads(result.text)
            lat.append(search_inf['documents'][0]['address']['y'])
            lng.append(search_inf['documents'][0]['address']['x'])
    resultset.append(lat)
    resultset.append(lng)
    return resultset

def scraping_data():
    url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"
    exceptClass = ['today']
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    table_html = soup.select('table.pc')
    ths = list(table_html[0].select('th'))
    gu_list = []
    for i in ths:
        gu_list.append(i.text)
    tds = list(table_html[0].findAll('td', class_=lambda x: x not in exceptClass))
    gu_num_list = []
    for i in tds:
        gu_num_list.append(i.text)
    
    gu_latlng = []
    headers = {"Authorization": "KakaoAK f65e7c08cbfe6221c3795ebb8da80931"} #지역검색 api
    for i in gu_list:
        print(i)
        location_name = i
        if i == '기타':
            coords = ['37.6600024610047','126.96954772211683']
            gu_latlng.append(coords)
        else:
            print(location_name)
            url = "https://dapi.kakao.com/v2/local/search/address.json?"
            query = "query="+ location_name
            url = url+query
            result = requests.get(url,headers = headers)
            search_inf = json.loads(result.text)
            print(search_inf)
            coords = [search_inf['documents'][0]['address']['y'],search_inf['documents'][0]['address']['x']]
            gu_latlng.append(coords)

    result = [gu_list,gu_num_list,gu_latlng]
    return result