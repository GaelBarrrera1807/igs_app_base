from django.contrib.auth.models import Permission

from igs_app_base.hiperforms import BaseHiperModelForm


class MainForm(BaseHiperModelForm):

    class Meta:
        model = Permission
        fields = "__all__"
        labels = {
            'name': 'Permiso',
            'content_type': 'Tipo',
            'codename': 'Código',
        }
