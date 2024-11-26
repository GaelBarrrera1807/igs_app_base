from django.contrib.auth.models import User
from django.db import models
from typing import Any

from igs_app_base.utils.utils import absolute_url
from igs_app_catalogo.models import TipoParametro

parametro_upload_to = "parametro_usuario"


class ParametroUsuario(models.Model):
    seccion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    valor_default = models.CharField(max_length=250, blank=True)
    tipo = models.ForeignKey(TipoParametro, models.PROTECT, '+')

    class Meta:
        ordering = ['seccion', 'nombre']
        unique_together = ['seccion', 'nombre']

    def __str__(self):
        if self.valor_default:
            return f"{self.nombre}: {self.valor_default}"
        return self.nombre

    def get_absolute_url(self):
        return absolute_url(self)

    @staticmethod
    def get_default(seccion: str, nombre: str) -> str:
        return ParametroUsuario.objects.get(
            seccion=seccion, nombre=nombre).valor_default

    @staticmethod
    def get_valor(user: User, seccion: str, nombre: str) -> str | int:
        pu = ParametroUsuario.objects.filter(seccion=seccion, nombre=nombre)
        if not pu.exists():
            return f"Parámetro de Usuario no encontrado {seccion}|{nombre}"
        puv = ParametroUsuarioValor.objects.filter(
            user=user, parametro=pu[0])
        val = puv[0].valor if puv.exists() else pu[0].valor_default
        if pu[0].tipo.pk == TipoParametro.objects.get(tipo_interno='INTEGER'):
            return int(val)
        return val

    @staticmethod
    def set_valor(
            user: User, seccion: str, nombre: str, valor: str | Any) -> bool:
        pu = ParametroUsuario.objects.filter(seccion=seccion, nombre=nombre)
        if not pu.exists():
            return False
        puv = ParametroUsuarioValor.objects.get_or_create(
            user=user, parametro=pu[0])
        puv.valor = str(valor)
        puv.save()
        return True


class ParametroUsuarioValor(models.Model):
    user = models.ForeignKey(User, models.CASCADE, '+')
    parametro = models.ForeignKey(ParametroUsuario, models.CASCADE, '+')
    valor = models.CharField(max_length=250)

    class Meta:
        ordering = ['user', 'parametro', 'valor']
        unique_together = ['user', 'parametro']

    def __str__(self):
        return self.valor

    def get_absolute_url(self):
        return absolute_url(self)

    @staticmethod
    def get(seccion: str, nombre: str, username: str) -> str:
        user = User.objects.filter(username=username)
        pu = ParametroUsuario.objects.filter(seccion=seccion, nomre=nombre)
        if not pu.exists():
            return f"Parámetro de Usuario no encontrado: {seccion}|{nombre}"
        if not user.exists():
            return pu[0].valor_default
        puv = ParametroUsuarioValor.objects.filter(
            parametro=pu[0], user=user[0])
        if not puv.exists():
            return pu[0].valor_default
        return puv[0].valor
