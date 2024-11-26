from typing import Any
from typing import Iterable

from django import template
from django.contrib.auth.models import User

from igs_app_base.models import App
from igs_app_base.utils.utils import get_user_from_context

register = template.Library()


@register.inclusion_tag('menu_helpers/list_opc.html', takes_context=True)
def print_menuopc_adm(context, opcion, nivel=-1) -> dict:
    nivel += 1
    return {'nivel': nivel, 'reg': opcion}


@register.simple_tag
def app_name(app: str = None) -> str:
    if app and isinstance(app, str):
        app = App.objects.filter(nombre=app)
        if app.exists():
            mnuopc = app[0].menuopc
            if mnuopc:
                return mnuopc.nombre
    return ""


@register.inclusion_tag('menu_helpers/menu_opc.html', takes_context=True)
def main_menu(
        context: Any, opciones: Iterable = None, nivel: int = 0,
        user_pk: User | int = 0, app: str = None, parent: str = "") -> dict:
    user = get_user_from_context(context, user_pk)
    if nivel == 0 and user is None:
        return {}
    if opciones is None:
        nivel = 1
        opciones = list()
        if app:
            app_obj = App.objects.filter(nombre=app)
            if app_obj.exists() and app_obj[0].menuopc:
                opciones = list(app_obj[0].menuopc.hijos.all())
    else:
        nivel += 1
    opciones = [mnuopc for mnuopc in opciones if mnuopc.user_has_option(user)]
    return {
        'nivel': nivel, 'opciones': opciones, 'user_pk': user.pk,
        'app': app, 'parent': parent}


@register.inclusion_tag(
    'menu_helpers/display_apps.html', takes_context=True)
def display_apps(
        context: Any, user_pk: User | int = 0, hidden: bool = False,
        custom_template: str = ""):
    user = get_user_from_context(context, user_pk)
    if user is None:
        return {}
    apps = App.objects.filter(display_as_app=not hidden)
    return {
        'apps': [
            app.menuopc
            for app in apps
            if app.menuopc is not None and app.menuopc.user_has_option(user)],
        'hidden': hidden,
        'template': custom_template
    }
