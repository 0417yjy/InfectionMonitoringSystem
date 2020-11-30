
# 55726a505564796436337345506d44 인증
import requests
from bs4 import BeautifulSoup
import time
import json

# 도구 - 메세지 템플릿 해서 템플릿 생성 후 Rest API - 메시지 에서 액세스 토큰 발급
KAKAO_TOKEN = "s3llEZoge5LsusPXEubqI6kHafztiaeYcjcuIQopcFEAAAF2GlZblQ"
send_lists = []

def send_to_kakao(text):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

def search():
    url2="https://www.edaily.co.kr/article/society"
    r=requests.get(url2)
    bs=BeautifulSoup(r.content,'lxml')
    divs=bs.select("ul.newsbox_texts") #select의 결과는 list이다
    for x in divs:
        if "코로나" in str(x) and "확진" in str(x):
            a=[]
            a.append(str(x))
            if count==0:
                b.append(str(x))

            if count==0:
                for z in a:
                    send_to_kakao(str(z))
            if count>0:
                for u in a:
                    if u not in b:
                        send_to_kakao(str(u))

            if str(x) not in b:
                b.append(str(x))

if __name__== "__main__":
    global count
    count=0
    a=[]
    b=[]
    while True:
        print(count)
        search()
        count+=1
        time.sleep(60) #1시간에 한번씩 검사해서 알림
