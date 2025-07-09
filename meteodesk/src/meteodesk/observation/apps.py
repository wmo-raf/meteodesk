from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ObservationConfig(AppConfig):
    name = 'meteodesk.observation'
    label = "meteodeskobs"
    verbose_name = _("MeteoDesk Observations")
    default_auto_field = 'django.db.models.BigAutoField'
