from django.apps import AppConfig


class EventsSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events_site'

    def ready(self):
        import events_site.signals