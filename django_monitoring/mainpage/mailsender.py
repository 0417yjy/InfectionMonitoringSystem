from django_monitoring.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def send_safe_mail(to, where, when):
    title = '[EDPS] ' + when + ": " + where + '확진자 발생'
    message = """
    안녕하세요, Team Lumos입니다.

    관심 지역으로 설정한 """ + where + """ 에서 확진자가 발생하였습니다.

    이 메시지는 자동으로 전송됩니다. 답장하지 마십시오.
    EDPS
    """

    send_mail(title, message, 'EDPS', to, fail_silently=False)

