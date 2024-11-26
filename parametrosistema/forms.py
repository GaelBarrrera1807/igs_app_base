from igs_app_base.hiperforms import BaseHiperModelForm

from .models import ParametroSistema


class MainForm(BaseHiperModelForm):

    class Meta:
        model = ParametroSistema
        fields = "__all__"
