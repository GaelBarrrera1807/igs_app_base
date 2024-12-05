from typing import Any

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from .crud import PERM_2_ACTION


def model_perms(model: Any, blinder_model: str = None) -> dict:
    ct = ContentType.objects.get_for_model(model)
    model_name = blinder_model if blinder_model else str(ct.model)
    return {
        'create': f'{ct.app_label}.{PERM_2_ACTION["create"]}_{model_name}',
        'read': f'{ct.app_label}.{PERM_2_ACTION["read"]}_{model_name}',
        'update': f'{ct.app_label}.{PERM_2_ACTION["update"]}_{model_name}',
        'delete': f'{ct.app_label}.{PERM_2_ACTION["delete"]}_{model_name}',
        'list': f'{ct.app_label}.{PERM_2_ACTION["list"]}_{model_name}',
    }


def model_perms_4_user(
        model: Any, user: User, blinder_model: str = None) -> dict:
    perms = model_perms(model, blinder_model)
    return {
        'create': user.has_perm(perms['create']),
        'read': user.has_perm(perms['read']),
        'update': user.has_perm(perms['update']),
        'delete': user.has_perm(perms['delete']),
        'list': user.has_perm(perms['list']),
    }
