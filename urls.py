from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.urls import include
from django.urls import path
from django.urls import reverse

from .views import Migrate
from .vw_app import Administracion
from .vw_app import Configuracion

urlpatterns = [
    path('', include('igs_app_base.session.urls')),
    path(
        "migrar/",
        permission_required('auth.apply_migration', '/')(Migrate.as_view()),
        name="aplicar_migraciones_vw"),
    path('sql/', include('igs_app_base.sql.urls')),
    path(
        'parametro-de-sistema/',
        include('igs_app_base.parametrosistema.urls')),
    path(
        'parametro-de-usuario/',
        include('igs_app_base.parametrousuario.urls')),
    path('perfil-de-usuario/', include('igs_app_base.group.urls')),
    path('permiso-de-usuario/', include('igs_app_base.permission.urls')),
    path('usuario/', include('igs_app_base.user.urls')),
    path('menu-principal/', include("igs_app_base.menu.urls")),

    path(
        'configuracion/',
        login_required()(Configuracion.as_view()),
        name="idx_app_configuracion"),
    path(
        'administracion/',
        login_required()(Administracion.as_view()),
        name="idx_app_administracion"),
    ]
