from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import MainForm


class SQLView(TemplateView):
    app = "administrar"
    template_name = "utils/sql.html"
    titulo = "SQL"
    titulo_descripcion = None
    toolbar = None
    sql = ""
    getrows = True
    rows = None
    header = None
    error = None

    def execute_sql(self):
        self.sql = self.request.POST.get('sql', self.sql)
        self.getrows = self.request.POST.get('getrows', '') == "on"
        if self.sql:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(self.sql)
                    if self.getrows:
                        self.rows = cursor.fetchall()
                        self.header = [c[0] for c in cursor.description]
                except Exception as e:
                    self.error = str(e)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.execute_sql()
        context["titulo"] = self.titulo
        context["titulo_descripcion"] = self.titulo_descripcion
        context["toolbar_search"] = False
        context["toolbar"] = self.toolbar
        context["footer"] = False
        context["read_only"] = False
        context["alertas"] = []
        context["mensajes"] = []
        context["req_chart"] = False
        context["search_value"] = None
        context["forms"] = None
        context["without_btn_save"] = False
        context["app"] = self.app
        context['sql'] = self.sql
        context['getrows'] = self.getrows
        context['rows'] = self.rows
        context['header'] = self.header
        context['error'] = self.error
        context['forms'] = {'top': [{'form': MainForm(
            self.request.POST, initial={'sql': "", 'getrows': False})}]}
        return context

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class SQL2JSONView(SQLView):

    def post(self, *args, **kwargs):
        html_result = super().post(*args, **kwargs)
        if self.error:
            return html_result
        result = list
        if self.getrows:
            result = [dict(zip(self.header, row)) for row in self.rows]
        return JsonResponse(result, safe=False)
