from django_monitoring.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def send_safe_mail(to, where, when):
    # to: 받을 메일 주소 리스트 (예: ['example@email.com', 'example2@email.com', 'example3@email.com'])
    # where: 스트링 - 관심 지역 이름 (예: '서울시 중구')
    # when: 스트링 - 발생한 날짜 ('yyyy-mm-d')
    title = '[EDPS] ' + when + ": " + where + '확진자 발생'
    message = """
    안녕하세요, Team Lumos입니다.

    관심 지역으로 설정한 """ + where + """ 에서 확진자가 발생하였습니다.

    이 메시지는 자동으로 전송됩니다. 답장하지 마십시오.
    EDPS
    """

    send_mail(title, message, 'EDPS', to, fail_silently=False)

