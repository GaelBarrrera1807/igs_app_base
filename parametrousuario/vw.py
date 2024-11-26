from django.contrib.auth.models import User
from django.http import JsonResponse

from igs_app_base.views import GenericList
from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import ParametroUsuario
from .models import ParametroUsuarioValor

views = GenericViews(
    ParametroUsuario, "Parámetro de Usuario", "Parámetros de Usuario",
    "administrar", MainForm, MainForm, MainForm)


class Set(GenericList):
    model = ParametroUsuario

    def get(self, *args, **kwargs):
        return JsonResponse({
            'status': 'error',
            'msg': "Método no implementado"
        }, safe=False)

    def post(self, *args, **kwargs):
        seccion = self.request.POST.get('seccion')
        param = self.request.POST.get('parametro')
        username = self.request.POST.get('user')
        valor = self.request.POST.get('value')
        res = {'status': 'error', 'extra': self.request.POST, 'res': None}
        if not (seccion and param and username and valor):
            res['msg'] = "Alguno de los parámetros requeridos no fue enviado"
        pu = self.model.objects.filter(seccion=seccion, nombre=param)
        user = User.objects.filter(username=username)
        if not pu.exists():
            res['msg'] = "El parámetro requerido no fue encontrado"
        if not user.exists():
            res['msg'] = "El usuario no fue encontrado"
        if res['msg']:
            return JsonResponse(res, safe=False)
        puv = ParametroUsuarioValor.objects.get_or_create(
            parametro=pu[0], user=user[0])[0]
        puv[0].valor = valor
        puv[0].save()
        res['status'] = "ok"
        res['msg'] = "Valor actualizado"
        return JsonResponse(res, safe=False)
