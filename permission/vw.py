from django.contrib.auth.models import Permission
from igs_app_base.views import GenericViews

from .forms import MainForm

views = GenericViews(
    Permission, "Permiso de Usuario", "Permisos de Usuario",
    'administrar', MainForm, MainForm, MainForm)
