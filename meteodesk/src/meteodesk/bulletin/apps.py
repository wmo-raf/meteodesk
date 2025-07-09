from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BulletinConfig(AppConfig):
    name = 'meteodesk.bulletin'
    label = "meteodeskbulletin"
    verbose_name = _("MeteoDesk Bulletins")
    default_auto_field = 'django.db.models.BigAutoField'
