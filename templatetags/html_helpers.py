from typing import Any
import urllib.request

from django import template
from django.template.loader import get_template

from igs_app_base.utils.utils import get_apps

register = template.Library()


@register.inclusion_tag('html/helpers/app_internal_link.html')
def link_apps_tag(filetype: str = "css"):
    return {'apps': get_apps(), 'type': filetype}


@register.filter
def template_exists(plantilla: str) -> bool:
    try:
        get_template(plantilla)
        return True
    except template.TemplateDoesNotExist:
        return False


@register.filter
def app_start_template_exists(app: str) -> bool:
    return template_exists(f"{app}/inicio.html")


@register.inclusion_tag('html/helpers/inicio_app.html', takes_context=True)
def app_start_templates_inclusion(context: Any) -> dict:
    res = {'apps': get_apps()}
    res.update(context.flatten())
    return res


@register.filter
def get_from_dict(data_dict, key):
    return data_dict.get(key)

@register.filter
def get_url_file_content(url):
    content = f"""/**********
    {url}
    **********/"""
    for line in urllib.request.urlopen(url):
        content += line.decode('utf-8')
    return content
