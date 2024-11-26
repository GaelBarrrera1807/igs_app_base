from django.contrib.auth.models import Group
from igs_app_base.views import GenericViews

from .forms import MainForm

views = GenericViews(
    Group, "Perfil de Usuario", "Perfiles de Usuario",
    'administrar', MainForm, MainForm, MainForm)
