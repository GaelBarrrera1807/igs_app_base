from igs_app_base.hiperforms import BaseHiperModelForm

from .models import ParametroUsuario


class MainForm(BaseHiperModelForm):

    class Meta:
        model = ParametroUsuario
        fields = "__all__"
