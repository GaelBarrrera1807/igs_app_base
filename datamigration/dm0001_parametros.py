from igs_app_base.models import ParametroSistema
from igs_app_catalogo.datamigration.dm0000_base import migration as m1
from igs_app_catalogo.models import TipoParametro


def migration():
    m1()
    ParametroSistema.objects.get_or_create(
        seccion="FormAcceso", nombre="main_logo",
        nombre_para_mostrar="Imagen para formulario de acceso",
        tipo=TipoParametro.objects.get(tipo_interno="PICTURE"))
    ParametroSistema.objects.get_or_create(
        seccion="SitioGeneral", nombre="favicon",
        nombre_para_mostrar="Icono (png) para favicon",
        tipo=TipoParametro.objects.get(tipo_interno="PICTURE"))
    ParametroSistema.objects.get_or_create(
        seccion="SitioGeneral", nombre="main_toolbar_logo",
        nombre_para_mostrar="Imagen para menú principal",
        tipo=TipoParametro.objects.get(tipo_interno="PICTURE"))
    ParametroSistema.objects.get_or_create(
        seccion="SitioGeneral", nombre="site_name",
        nombre_para_mostrar="Nombre del Sitio (menú principal)",
        valor="iGrowSoft",
        tipo=TipoParametro.objects.get(tipo_interno="STRING"))
    ParametroSistema.objects.get_or_create(
        seccion="SitioGeneral", nombre="site_title",
        nombre_para_mostrar="Título del Sitio",
        valor="iGrowSoft",
        tipo=TipoParametro.objects.get(tipo_interno="STRING"))
