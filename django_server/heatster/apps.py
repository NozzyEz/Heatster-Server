from django.apps import AppConfig


class HeatsterConfig(AppConfig):
    name = 'heatster'

    def ready(self):
        import heatster.signals