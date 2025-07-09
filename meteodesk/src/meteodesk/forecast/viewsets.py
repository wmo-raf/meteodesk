from django.urls import path
from wagtail.admin.viewsets.base import ViewSet

from .views import forecast_index


class ForecastViewSet(ViewSet):
    menu_label = "Forecasts"
    icon = "date"
    name = "forecast"
    
    def get_urlpatterns(self):
        return [
            path('', forecast_index, name='forecast_index'),
        ]
