from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class MenuOpc(models.Model):
    nombre = models.CharField(max_length=50)
    padre = models.ForeignKey(
        "MenuOpc", models.SET_NULL,
        related_name="hijos", null=True, blank=True)
    posicion = models.PositiveSmallIntegerField()
    vista = models.CharField(max_length=50, blank=True)
    permisos_requeridos = models.ManyToManyField(
        Permission, related_name="opc_menu",
        help_text="El usuario que tenga al menos uno de los permisos "
        "seleccionados tendrá acceso a la opción del menú", blank=True)

    class Meta:
        ordering = ['posicion', 'nombre']

    def __str__(self):
        return self.nombre

    @property
    def vista_url(self):
        if self.vista:
            try:
                return reverse(self.vista)
            except NoReverseMatch:
                pass
        return None

    def user_has_option(self, user: User):
        if len(self.hijos.all()) == 0:
            return len(self.permisos_requeridos.all()) == 0 \
                or any([
                    user.has_perm(p)
                    for p in self.permisos_requeridos.all()])
        return any([h.user_has_option(user) for h in self.hijos.all()])
