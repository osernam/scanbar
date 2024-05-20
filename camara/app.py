from django.apps import AppConfig


class CamaraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'camara'
    
    
    def ready(self):
        super().ready()
        from . import signals