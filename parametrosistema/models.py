from django.db import models
from django.utils.safestring import mark_safe

from igs_app_base.utils.utils import absolute_url
from igs_app_catalogo.models import TipoParametro

parametro_upload_to = "parametro_sistema"


class ParametroSistema(models.Model):
    seccion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    nombre_para_mostrar = models.CharField(max_length=100)
    valor = models.TextField(blank=True)
    tipo = models.ForeignKey(TipoParametro, models.PROTECT, "+")

    class Meta:
        ordering = ['seccion', 'nombre_para_mostrar']
        unique_together = ['seccion', 'nombre']
        permissions = [
            ("set_parametrosistema", "Establecer parámetros de sistema", ),
        ]

    def __str__(self):
        if self.valor:
            return f"{self.nombre_para_mostrar}: {self.valor}"
        return self.nombre_para_mostrar

    def get_absolute_url(self):
        return absolute_url(self)

    @property
    def widget(self) -> str:
        id = f'{ self.seccion }_{ self.nombre }'
        id_name = f'id="{id}" name="{id}"'
        cad = ""
        if self.tipo.tipo_interno == "TEXT":
            open_tag = f'<textarea {id_name} rows="10" class="form-control">'
            close_tag = f'</textarea>'
            cad = f'{open_tag}{self.valor}{close_tag}'
        else:
            input_widget = f'<input {id_name} class="form-control"'
            if self.tipo.tipo_interno in ["PICTURE", "FILE"]:
                cad = f'{input_widget} type="file" />'
            elif self.tipo.tipo_interno in ["STRING", "DECIMAL"]:
                cad = f'{input_widget} type="text" value="{self.valor}" />'
            elif self.tipo.tipo_interno == "INTEGER":
                cad = f'{input_widget} type="number" value="{self.valor}" />'
            else:
                cad = f'{ self }: { self.tipo }'
        return mark_safe(cad)

    @staticmethod
    def get(seccion, nombre):
        ps = ParametroSistema.objects.filter(seccion=seccion, nombre=nombre)
        if ps.exists():
            return ps[0].valor
        else:
            return f"Parámetro de Sistema no encontrado: {seccion} / {nombre}"
