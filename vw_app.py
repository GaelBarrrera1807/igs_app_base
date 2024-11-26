from .views import GenericAppRootView


class Configuracion(GenericAppRootView):
    app = "configuracion"
    titulo = "Configuracion"


class Administracion(GenericAppRootView):
    app = "administrar"
    titulo = "Administración"
