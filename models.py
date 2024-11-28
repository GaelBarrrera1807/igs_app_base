from typing import Any

from django.db import models

from .menu.models import MenuOpc
from .parametrosistema.models import ParametroSistema
from .parametrousuario.models import ParametroUsuario
from .parametrousuario.models import ParametroUsuarioValor
from .user.models import UserProfile


class App(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    posicion = models.PositiveSmallIntegerField(default=0)
    display_as_app = models.BooleanField(default=True)

    class Meta:
        ordering = ['posicion', 'nombre']

    def __str__(self):
        return self.nombre

    @property
    def menuopc(self) -> MenuOpc | None:
        mnuopc = MenuOpc.objects.filter(padre=None, posicion=self.posicion)
        return mnuopc[0] if mnuopc.exists() else None

    @staticmethod
    def get_by_name(nombre) -> Any | None:
        app = App.objects.filter(nombre=nombre)
        if app.exists():
            return app[0]
