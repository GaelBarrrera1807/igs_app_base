from django.contrib.auth.decorators import login_required
from django.urls import path

from .vw import Set
from .vw import views

obj = 'parametrousuario'
app_label = 'igs_app_base'

urlpatterns = views.create_urls(app_label) + [
    path(
        'establecer/',
        login_required()(
            Set.as_view()),
        name=f"{obj}_set")
]
