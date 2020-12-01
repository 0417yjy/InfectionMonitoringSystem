from django.apps import AppConfig


class MainpageConfig(AppConfig):
    name = 'mainpage'
    def ready(self):
        import mainpage.signals