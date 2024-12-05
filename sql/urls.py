from django.contrib.auth.decorators import permission_required
from django.urls import path

from .vw import SQL2JSONView
from .vw import SQLView

urlpatterns = [
    path(
        '',
        permission_required('auth.sql_exec_rows', '/')(SQLView.as_view()),
        name='sql_exec_rows'),
    path(
        '2json/',
        permission_required('auth.sql_exec_json', '/')(SQL2JSONView.as_view()),
        name='sql_exec_json'),
    path(
        '2-json/',
        SQL2JSONView.as_view(),
        name='sql_exec_json_out'),
    ]
