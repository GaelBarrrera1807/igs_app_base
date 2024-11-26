from django import forms
from django.contrib.auth import authenticate

from igs_app_base.hiperforms import BaseHiperForm


class MainForm(BaseHiperForm):
    username = forms.CharField(
        max_length=50, label="Usuario",
        widget=forms.TextInput(attrs={'autofocus': "autofocus"}))
    password = forms.CharField(
        max_length=50, label="Contraseña",
        widget=forms.PasswordInput())

    def clean(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'])
        if not self.user or not self.user.is_active:
            raise forms.ValidationError(
                "El usuario o la contraseña no son válidos.")
        return self.cleaned_data
