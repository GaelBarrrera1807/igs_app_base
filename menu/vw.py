from igs_app_base.views import GenericViews, GenericList

from .models import MenuOpc
from .forms import MainForm

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
