from django import template
from django.utils.safestring import mark_safe

from igs_app_base.models import ParametroSistema
from igs_app_base.models import ParametroUsuarioValor

register = template.Library()


@register.simple_tag
def parametro_de_sistema(seccion, nombre):
    return mark_safe(ParametroSistema.get(seccion, nombre))


@register.simple_tag
def parametro_de_usuario(seccion, nombre, username):
    return mark_safe(ParametroUsuarioValor.get(seccion, nombre, username))
