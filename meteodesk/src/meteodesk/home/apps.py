from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = 'meteodesk.home'
    label = "meteodeskhome"
    verbose_name = _("MeteoDesk Forecast")
    default_auto_field = 'django.db.models.BigAutoField'
