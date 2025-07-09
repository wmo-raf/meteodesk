from django.urls import path
from wagtail.admin.viewsets.base import ViewSet

from .views import obs_index


class ObservationViewSet(ViewSet):
    menu_label = "Observations"
    icon = "date"
    name = "obs"
    
    def get_urlpatterns(self):
        return [
            path('', obs_index, name='obs_index'),
        ]
