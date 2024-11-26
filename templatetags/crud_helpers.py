from django import template
from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe

from igs_app_base.utils.crud import ACTION_ICONS
from igs_app_base.utils.crud import ACTION_LABELS
from igs_app_base.utils.crud import CRUD_ICONS
from igs_app_base.utils.crud import CRUD_LABELS

register = template.Library()


def smart_button(
        icon: str, label: str, label_and_icon: bool = False) -> SafeString:
    label_tag = f'<span class="d-none d-sm-inline">{label}</span>'
    return mark_safe(
        f'{icon} {label_tag}' if label_and_icon else icon)


@register.simple_tag
def crud_icon(operador: str) -> str | SafeString:
    try:
        return mark_safe(CRUD_ICONS[operador])
    except KeyError:
        return operador


@register.simple_tag
def crud_label(operador: str) -> str | SafeString:
    try:
        return mark_safe(CRUD_LABELS[operador])
    except KeyError:
        return operador


@register.simple_tag
def crud_smart_button(operador, label_and_icon: bool = False) -> SafeString:
    return smart_button(
        crud_icon(operador), crud_label(operador), label_and_icon)


@register.simple_tag
def action_icon(operador: str) -> str | SafeString:
    try:
        return mark_safe(ACTION_ICONS[operador])
    except KeyError:
        return operador


@register.simple_tag
def action_label(operador: str) -> str | SafeString:
    try:
        return mark_safe(ACTION_LABELS[operador])
    except KeyError:
        return operador


@register.simple_tag
def action_smart_button(operador, label_and_icon: bool = False) -> SafeString:
    return smart_button(
        action_icon(operador), action_label(operador), label_and_icon)
