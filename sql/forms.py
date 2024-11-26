from django import forms

from igs_app_base.hiperforms import BaseHiperForm


class MainForm(BaseHiperForm):
    sql = forms.CharField(widget=forms.Textarea)
    getrows = forms.BooleanField(
        widget=forms.CheckboxInput, label="Retorna registros", required=False)
