from wagtail import hooks

from .viewsets import MeteoDeskViewSetGroup


@hooks.register("register_admin_viewset")
def register_viewset():
    return MeteoDeskViewSetGroup()
