from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MeteoDeskAppConfig(AppConfig):
    name = "meteodesk"
    label = "meteodeskcore"
    verbose_name = _("MeteoDesk core")
    default_auto_field = "django.db.models.AutoField"
    
    def ready(self):
        pass
