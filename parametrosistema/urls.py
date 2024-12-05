from django.contrib.auth.decorators import permission_required
from django.urls import path

from .vw import Set
from .vw import views

obj = 'parametrosistema'
app_label = 'igs_app_base'

urlpatterns = views.create_urls(app_label) + [
    path(
        'establecer/',
        permission_required(f'{app_label}.set_{obj}', '/')(
            Set.as_view()),
        name=f"{obj}_set")
]
