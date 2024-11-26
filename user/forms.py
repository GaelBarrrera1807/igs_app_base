from django import forms
from django.contrib.auth.models import User

from igs_app_base.hiperforms import BaseHiperForm
from igs_app_base.hiperforms import BaseHiperModelForm


class TopReadForm(BaseHiperModelForm):

    class Meta:
        model = User
        fields = ['username']
        labels = {'username': 'Usuario'}


class TopCreateForm(BaseHiperModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Usuario',
            'password': 'Contraseña'
        }
        widgets = {'password': forms.PasswordInput()}


class LeftForm(BaseHiperModelForm):
    apellido_materno = forms.CharField(max_length=50, required=False)
    telefono = forms.CharField(max_length=10, required=False)
    celular = forms.CharField(max_length=10, required=False)
    whatsapp = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido paterno",
            "email": "EMail",
        }

    field_order = [
        "first_name", "last_name", "apellido_materno",
        "email",
        "telefono", "celular", "whatsapp",
    ]


class RightForm(BaseHiperModelForm):

    class Meta:
        model = User
        fields = ["is_staff", "is_active", "is_superuser", "groups"]
        labels = {
            "is_staff": "Staff",
            "is_active": "Activo",
            "is_superuser": "SuperUsuario",
            "groups": "Perfiles"
        }
        widgets = {"groups": forms.CheckboxSelectMultiple()}


class BottomForm(BaseHiperModelForm):

    class Meta:
        model = User
        fields = ["user_permissions"]
        labels = {"user_permissions": "Permisos Extra"}
        widgets = {"user_permissions": forms.CheckboxSelectMultiple()}


class CreateForm(BaseHiperModelForm):
    apellido_materno = forms.CharField(max_length=50, required=False)
    telefono = forms.CharField(max_length=10, required=False)
    celular = forms.CharField(max_length=10, required=False)
    whatsapp = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = [
            "username", "password",
            "is_superuser", "is_staff", "is_active",
            "first_name", "last_name",
            "email", "groups", "user_permissions",
        ]


class UpdateForm(BaseHiperModelForm):
    apellido_materno = forms.CharField(max_length=50, required=False)
    telefono = forms.CharField(max_length=10, required=False)
    celular = forms.CharField(max_length=10, required=False)
    whatsapp = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = [
            "is_superuser", "is_staff", "is_active",
            "first_name", "last_name",
            "email", "groups", "user_permissions",
        ]


class ResetPasswordForm(BaseHiperForm):
    username = forms.CharField(required=True, max_length=50, label="Usuario")
    password = forms.CharField(
        required=True, max_length=50,
        label="Contraseña", widget=forms.PasswordInput())


class ResetPasswordByMeForm(BaseHiperForm):
    username = forms.CharField(required=True, max_length=50, label="Usuario")
    password = forms.CharField(
        required=False, max_length=50,
        label="Contraseña", widget=forms.PasswordInput())
