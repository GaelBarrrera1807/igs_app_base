from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import TemplateView

from igs_app_base.views import GenericCreate
from igs_app_base.views import GenericDelete
from igs_app_base.views import GenericDeleteMany
from igs_app_base.views import GenericList
from igs_app_base.views import GenericRead
from igs_app_base.views import GenericUpdate

from .forms import BottomForm
from .forms import CreateForm
from .forms import LeftForm
from .forms import ResetPasswordByMeForm
from .forms import ResetPasswordForm
from .forms import RightForm
from .forms import TopCreateForm
from .forms import TopReadForm
from .forms import UpdateForm
from .models import UserProfile

titulo = "Usuario"
app = "administrar"


def create_profile(user: User) -> User:
    try:
        user.profile
    except user._meta.model.profile.RelatedObjectDoesNotExist:
        user.profile = UserProfile.objects.get_or_create(user=user)
    finally:
        return user


class List(GenericList):
    model = User
    titulo = "Usuarios"
    app = app


class Create(GenericCreate):
    model = User
    titulo = titulo
    app = app
    form_class = CreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"] = {
            'top': [{'form': TopCreateForm()}],
            'left': [{'form': LeftForm()}],
            'right': [{'form': RightForm()}],
            'bottom': [{'form': BottomForm()}],
        }
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.set_password(self.object.password)
        self.object.groups.add(Group.objects.get_or_create(name="Basico")[0])
        create_profile(self.object)
        self.object.save()
        self.object.profile.apellido_materno = self.request.POST.get(
            'apellido_materno', '')
        self.object.profile.telefono = self.request.POST.get(
            'telefono', '')
        self.object.profile.celular = self.request.POST.get(
            'celular', '')
        self.object.profile.whatsapp = self.request.POST.get(
            'whatsapp', '')
        self.object.profile.save()
        return response


class Read(GenericRead):
    model = User
    titulo = titulo
    app = app
    form_class = UpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        create_profile(self.object)
        context["forms"] = {
            'top': [{'form': TopReadForm(instance=self.object)}],
            'left': [{'form': LeftForm(instance=self.object, initial={
                'apellido_materno': self.object.profile.apellido_materno,
                'telefono': self.object.profile.telefono,
                'celular': self.object.profile.celular,
                'whatsapp': self.object.profile.whatsapp,
            })}],
            'right': [{'form': RightForm(instance=self.object)}],
            'bottom': [{'form': BottomForm(instance=self.object)}],
        }
        return context


class Update(GenericUpdate):
    model = User
    titulo = titulo
    app = app
    form_class = UpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        create_profile(self.object)
        context["forms"] = {
            'top': [{'form': TopReadForm(instance=self.object)}],
            'left': [{'form': LeftForm(instance=self.object, initial={
                'apellido_materno': self.object.profile.apellido_materno,
                'telefono': self.object.profile.telefono,
                'celular': self.object.profile.celular,
                'whatsapp': self.object.profile.whatsapp,
            })}],
            'right': [{'form': RightForm(instance=self.object)}],
            'bottom': [{'form': BottomForm(instance=self.object)}],
        }
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.profile.apellido_materno = self.request.POST.get(
            'apellido_materno', '')
        self.object.profile.telefono = self.request.POST.get(
            'telefono', '')
        self.object.profile.celular = self.request.POST.get(
            'celular', '')
        self.object.profile.whatsapp = self.request.POST.get(
            'whatsapp', '')
        self.object.profile.save()
        return response


class Delete(GenericDelete):
    model = User
    titulo = titulo
    app = app


class DeleteMany(GenericDeleteMany):
    model = User
    titulo = titulo
    app = app


class ResetPassword(TemplateView):
    model = User
    titulo = "Restaurar Contraseña"
    app = "configuracion"
    form_class = ResetPasswordForm
    template_name = "html/form.html"
    status = None

    def get_object(self, username):
        self.object = None
        if username:
            obj = self.model.objects.filter(username=username)
            if obj.exists():
                self.object = obj[0]
            else:
                self.status = {
                    'msg': f"No existe el usuario {username}",
                    'type': 'danger', 'dismissible': True,
                }
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = self.titulo
        context["titulo_descripcion"] = str(self.object) if (
            self.object) else None
        context["toolbar_search"] = None
        context["toolbar"] = None
        context["footer"] = False
        context["read_only"] = False
        context["alertas"] = []
        context["mensajes"] = [self.status, ] if self.status else []
        context["req_chart"] = False
        context["search_value"] = None
        context["without_btn_save"] = False
        context["app"] = self.app
        if self.object:
            context["forms"] = {
                'top': [{'form': ResetPasswordForm(
                    initial={'username': self.object.username})}],
            }
        else:
            context["forms"] = {
                'top': [{'form': ResetPasswordForm()}],
            }
        return context

    def get(self, request, *args, **kwargs):
        self.get_object(kwargs.get('username'))
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        if not (username and password):
            return self.get(request, *args, **kwargs)
        if self.get_object(username):
            self.object.set_password(password)
            self.object.save()
            self.status = {
                'msg': f"Password Re-establecido para {username}",
                'type': 'success', 'dismissible': True
            }
        return self.get(request, *args, **kwargs)


class Me(Update):
    titulo = "Mi Perfil"
    form_class = LeftForm
    status = None
    app = ""

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        create_profile(self.object)
        context["forms"] = {
            'top': [{'form': ResetPasswordByMeForm(
                initial={'username': self.object.username})}],
            'bottom': [{'form': LeftForm(instance=self.object, initial={
                'apellido_materno': self.object.profile.apellido_materno,
                'telefono': self.object.profile.telefono,
                'celular': self.object.profile.celular,
                'whatsapp': self.object.profile.whatsapp,
            })}],
        }
        context['titulo_descripcion'] = str(self.object.profile)
        context["mensajes"] = [self.status, ] if self.status else []
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        pwd = self.request.POST.get('password')
        if pwd:
            self.object.set_password(pwd)
            self.object.save()
        self.status = {
            'msg': f"Información actualizada",
            'type': 'success', 'dismissible': True
        }
        return response

    def get_success_url(self):
        return reverse("user_me")
