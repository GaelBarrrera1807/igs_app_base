from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType

from igs_app_base.models import App
from igs_app_base.user.models import UserProfile
from igs_app_base.utils.utils import add_or_create_menuopc


def migration():
    Group.objects.get_or_create(name="Administrador")
    Group.objects.get_or_create(name="Pruebas")
    Group.objects.get_or_create(name="Basico")

    admin = User.objects.filter(username="admin")
    if not admin.exists():
        admin = User.objects.create(
            username="admin", is_superuser=True, is_staff=True)
        admin.set_password('change_me')
        admin.save()
    else:
        admin = admin[0]
    UserProfile.objects.get_or_create(user=admin)

    app, created = App.objects.get_or_create(nombre="configuracion")
    if created:
        app.posicion = 1000
        app.save()

    app, created = App.objects.get_or_create(nombre="administrar")
    if created:
        app.posicion = 1001
        app.save()

    add_or_create_menuopc(
        "Salir", 9000,
        None, None, None, "session_logout")

    conf = add_or_create_menuopc(
        "Configuracion", 1000,
        None, None, None, "idx_app_configuracion")

    add_or_create_menuopc(
        "Re-establecer Contraseña", 1, conf, None,
        [Permission.objects.get_or_create(
            codename="reset_password", name="Re-establecer Contraseña",
            content_type=ContentType.objects.get_for_model(User))[0]],
        "user_reset_password")

    add_or_create_menuopc(
        "Parámetros de Sistema", 2, conf, None,
        [Permission.objects.get(codename="set_parametrosistema"), ],
        "parametrosistema_set")

    add_or_create_menuopc(
        "Aplicar Migracion de Datos", 100, conf,
        None,
        [Permission.objects.get_or_create(
            codename="apply_migration", name="Aplicar migraciones",
            content_type=ContentType.objects.get_for_model(Permission))[0], ],
        "aplicar_migraciones_vw")

    adm = add_or_create_menuopc(
        "Administrar", 1001, None, None,
        None, "idx_app_administracion")

    add_or_create_menuopc(
        "Usuarios", 1, adm, "user")
    add_or_create_menuopc(
        "Perfiles de Usuario", 2, adm, "group")
    add_or_create_menuopc(
        "Permisos de Usuario", 3, adm, "permission")
    add_or_create_menuopc(
        "Menú Principal", 4, adm, "menuopc")
    add_or_create_menuopc(
        "Parámetros de Sistema", 5, adm, "parametrosistema")
    add_or_create_menuopc(
        "Parámetros de Usuario", 6, adm, "parametrousuario")

    add_or_create_menuopc(
        "SQL", 51, adm, None,
        [Permission.objects.get_or_create(
            name="Ejecutar instruciones SQL",
            content_type=ContentType.objects.get_for_model(Permission),
            codename="sql_exec_rows")[0], ],
        "sql_exec_rows")

    add_or_create_menuopc(
        "SQL a JSON", 52, adm, None,
        [Permission.objects.get_or_create(
            name="Ejecutar instruciones SQL - JSON",
            content_type=ContentType.objects.get_for_model(Permission),
            codename="sql_exec_json")[0], ],
        "sql_exec_json")
