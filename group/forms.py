from django import forms
from django.contrib.auth.models import Group

from igs_app_base.hiperforms import BaseHiperModelForm


class MainForm(BaseHiperModelForm):

    class Meta:
        model = Group
        fields = "__all__"
        labels: {
            'name': "Perfil",
            'permissions': "Permisos",
        }
        widgets = {
            'permissions': forms.CheckboxSelectMultiple()
        }
