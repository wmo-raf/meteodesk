from django.urls import path
from wagtail.admin.viewsets.base import ViewSet

from .views import bulletin_index


class BulletinViewSet(ViewSet):
    menu_label = "Bulletins"
    icon = "date"
    name = "bulletin"
    
    def get_urlpatterns(self):
        return [
            path('', bulletin_index, name='bulletin_index'),
        ]
