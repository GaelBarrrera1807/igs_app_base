from django.contrib.auth.models import User
from django.db import models
from typing import Any


class UserProfile(models.Model):
    apellido_materno = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    celular = models.CharField(max_length=10, blank=True)
    whatsapp = models.CharField(
        max_length=10, blank=True, verbose_name="What's App")
    user = models.OneToOneField(User, models.CASCADE, related_name="profile")

    class Meta:
        ordering = ['telefono', 'celular', 'whatsapp', ]

    def __str__(self):
        name = f"{self.user.get_full_name()} {self.apellido_materno}".strip()
        return name if name else self.user.username

    def can(
            self, perms: list | str, type_result: str = "string"
            ) -> bool | str | int:

        def is_iterable(value: Any) -> bool:
            try:
                iter(value)
                return True
            finally:
                return False

        if isinstance(perms, str) or not is_iterable(perms):
            res = self.user.has_perm(perms)
        else:
            res = any([self.user.has_perm(perm) for perm in perms])

        if type_result in ["str", "string"]:
            return "true" if res else "false"
        elif type_result in ["int", "integer", "number", "numeric"]:
            return 1 if res else 0
        return res      # when type_result in ["bool", "boolean"]
