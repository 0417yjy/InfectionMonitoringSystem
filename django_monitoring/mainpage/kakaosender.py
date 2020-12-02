

# 도구 - 메세지 템플릿 해서 템플릿 생성 후 Rest API - 메시지 에서 액세스 토큰 발급

import json
import requests
#from models import Subscriber

def send_to_kakao():
    access_token = "" # 인증키 받아옴
    send_lists = []
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
# 사용자 토큰
    headers = {
        "Authorization": "Bearer " + access_token
        }


    data = {
        "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "안녕하세요, Team Lumos 입니다.   관심 지역에서 확진자가 발생하였습니다.",
                                     "link" : {
                                                 "web_url" : "http://127.0.0.1:8000/mainpage/"
                                              }
                                              })
                                              }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

send_to_kakao()
