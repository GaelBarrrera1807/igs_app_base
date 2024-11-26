from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.urls import path

from igs_app_base.utils.utils import create_view_urls

from .vw import Create
from .vw import Delete
from .vw import DeleteMany
from .vw import List
from .vw import Me
from .vw import Read
from .vw import ResetPassword
from .vw import Update

obj = 'user'
app_label = 'auth'

urlpatterns = create_view_urls(
    "auth", "user",
    List, Create, Update, Read, DeleteMany, Delete) + [
    path(
        'reestablecer-password/',
        permission_required(f'{app_label}.reset_password')(
            ResetPassword.as_view()),
        name=f"{obj}_reset_password"),
    path(
        'reestablecer-password/<str:username>',
        permission_required(f'{app_label}.reset_password')(
            ResetPassword.as_view()),
        name=f"{obj}_reset_password"),
    path(
        'mi-perfil/',
        login_required()(
            Me.as_view()),
        name=f"{obj}_me"),
]
