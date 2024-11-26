import os.path

from django.conf import settings

from igs_app_base.utils.utils import create_path
from igs_app_base.views import GenericList
from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import ParametroSistema
from .models import parametro_upload_to

views = GenericViews(
    ParametroSistema, "Parámetro de Sistema", "Parámetros de Sistema",
    "administrar", MainForm, MainForm, MainForm)


class Set(GenericList):
    template_name = "igs_app_base/parametrosistema_set.html"
    titulo = "Parámetros de Sistema"
    titulo_descripcion = "(Establecer)"
    model = ParametroSistema
    app = "configuracion"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["toolbar"] = None
        return context

    def post(self, request, *args, **kwargs):
        for param in self.model.objects.all():
            if (param.tipo.tipo_interno == "INTEGER"
                    or param.tipo.tipo_interno == "STRING"
                    or param.tipo.tipo_interno == "DECIMAL"
                    or param.tipo.tipo_interno == "TEXT"):
                valor = self.request.POST.get(
                    f"{param.seccion}_{param.nombre}")
                if valor is not None:
                    param.valor = valor
            elif (param.tipo.tipo_interno == "PICTURE"
                    or param.tipo.tipo_interno == "FILE"):
                file = self.request.FILES.get(
                    f"{param.seccion}_{param.nombre}")
                if file is not None:
                    pparam = os.path.join(
                        settings.BASE_DIR, settings.MEDIA_ROOT,
                        parametro_upload_to)
                    create_path(pparam)
                    fname = os.path.join(pparam, file.name.replace(" ", "_"))
                    bname = os.path.splitext(fname)[0]
                    cont = 0
                    while os.path.isfile(fname):
                        cont += 1
                        fname = os.path.join(
                            pparam,
                            f"{bname}_{cont:04d}{os.path.splitext(fname)[1]}")
                    with open(fname, 'wb+') as f:
                        try:
                            [f.write(chunk) for chunk in file.chunks]
                        except Exception:
                            f.write(file.read())
                    param.valor = os.path.join(
                        parametro_upload_to, os.path.basename(fname))
            param.save()
        return self.get(request, *args, **kwargs)
