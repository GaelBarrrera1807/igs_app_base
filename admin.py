from django.contrib import admin

from .models import App
from .models import MenuOpc
from .models import ParametroSistema
from .models import ParametroUsuario
from .models import ParametroUsuarioValor
from .models import UserProfile


@admin.register(MenuOpc)
class MenuOpcAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'padre', 'posicion', 'vista')
    list_filter = ('padre',)
    raw_id_fields = ('permisos_requeridos',)


@admin.register(ParametroSistema)
class ParametroSistemaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'seccion',
        'nombre',
        'valor',
    )
    list_filter = ('tipo', 'seccion')


@admin.register(ParametroUsuario)
class ParametroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'seccion', 'nombre', 'valor_default', 'tipo')
    list_filter = ('tipo', 'seccion')


@admin.register(ParametroUsuarioValor)
class ParametroUsuarioValorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__profile', 'parametro', 'parametro__seccion')
    list_filter = ('user', 'parametro', 'parametro__seccion')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'user__first_name',
        'user__last_name',
        'apellido_materno',
    )
    list_filter = ('user',)


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'posicion', 'display_as_app')
    list_filter = ('display_as_app',)
