from django.apps import AppConfig


class {{ camel_case_app_name }}Config(AppConfig):
    name = '{{ app_name }}'

    def ready(self):
        # uncomment these to activate signals
        pass
