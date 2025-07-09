from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ForecastConfig(AppConfig):
    name = 'meteodesk.forecast'
    label = "meteodeskforecast"
    verbose_name = _("MeteoDesk Forecasts")
    default_auto_field = 'django.db.models.BigAutoField'
