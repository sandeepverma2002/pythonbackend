from django.apps import AppConfig


class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'


# cards/apps.py

from django.apps import AppConfig
from .auto_ping import keep_alive
import threading

class CardsConfig(AppConfig):
    name = 'cards'

    def ready(self):
        threading.Thread(target=keep_alive, daemon=True).start()
