from igs_app_base.views import GenericList
from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import MenuOpc

views = GenericViews(
    MenuOpc, "Opcion de Menú Principal", "Menú Principal",
    "administrar", MainForm, MainForm, MainForm)


class List(GenericList):
    model = MenuOpc
    titulo = "Meú Principal"
    app = "administrar"

    def get_queryset(self):
        return self.model.objects.filter(padre=None)


views.List = List
