from django.urls import path
from wagtail.admin.viewsets import ViewSetGroup
from wagtail.admin.viewsets.base import ViewSet

from .bulletin.viewsets import BulletinViewSet
from .forecast.viewsets import ForecastViewSet
from .observation.viewsets import ObservationViewSet
from .views import weather_variables_settings


class WeatherVariablesViewSet(ViewSet):
    menu_label = "Weather Variables"
    icon = "cog"
    name = "weather-settings"
    
    def get_urlpatterns(self):
        return [
            path('', weather_variables_settings, name='weather_variables_index'),
        ]


class SettingsViewSetGroup(ViewSetGroup):
    menu_label = "Settings"
    menu_icon = "cog"
    add_to_admin_menu = False
    
    # You can specify instances or subclasses of `ViewSet` in `items`.
    items = [
        WeatherVariablesViewSet(),
    ]


class MeteoDeskViewSetGroup(ViewSetGroup):
    menu_label = "MeteoDesk"
    menu_icon = "desktop"
    add_to_admin_menu = True
    
    # You can specify instances or subclasses of `ViewSet` in `items`.
    items = [
        ForecastViewSet(),
        ObservationViewSet(),
        BulletinViewSet(),
        SettingsViewSetGroup()
    ]
