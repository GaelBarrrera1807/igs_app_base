from django import forms

from .models import MenuOpc
from igs_app_base.hiperforms import BaseHiperModelForm


class MainForm(BaseHiperModelForm):

    class Meta:
        model = MenuOpc
        fields = "__all__"
        widgets = {'permisos_requeridos': forms.CheckboxSelectMultiple()}
