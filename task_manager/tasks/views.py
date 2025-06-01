from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from ..mixins import AuthRequiredMessageMixin  # , IsOwnerMixin
from .forms import LabelForm, LabelFormDelete, StatusForm, StatusFormDelete
from .models import Label, Status


class SimpleIndexView(AuthRequiredMessageMixin, View):

    model = None
    term = ''
    terms = ''
    term_url = ''
    term_update_url = ''
    term_delete_url = ''

    def get(self, request, *args, **kwargs):
        items = list(self.model.objects.all())
        return render(
            request,
            'tasks/index_simple.html',
            context={
                'items': items,
                'term': self.term,
                'terms': self.terms,
                'term_url': self.term_url,
                'term_update_url': self.term_update_url,
                'term_delete_url': self.term_delete_url,
            },
        )


class StatusIndexView(SimpleIndexView):
    model = Status
    term = 'статус'
    terms = 'Статусы'
    term_url = 'tasks:create_status'
    term_update_url = 'tasks:update_status'
    term_delete_url = 'tasks:delete_status'


class LabelIndexView(SimpleIndexView):
    model = Label
    term = 'метку'
    terms = 'Метки'
    term_url = 'tasks:create_label'
    term_update_url = 'tasks:update_label'
    term_delete_url = 'tasks:delete_label'


class SimpleFormCreateView(AuthRequiredMessageMixin, View):

    form = None
    form_title = ''
    btn_title = ''
    succ_mess = ''
    list_url = ''

    def get(self, request, *args, **kwargs):
        form = self.form()  #StatusForm()
        return render(
            request,
            'tasks/create_simple.html',
            {
                'form': form,
                'form_title': self.form_title,
                'btn_title': self.btn_title
            })

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, self.succ_mess)
            return redirect(self.list_url)

        return render(
            request,
            'tasks/create_simple.html',
            {
                'form': form,
                'form_title': self.form_title,
                'btn_title': self.btn_title
            })


class StatusFormCreateView(SimpleFormCreateView):
    form = StatusForm
    form_title = 'Создать статус'
    btn_title = 'Создать'
    succ_mess = 'Статус успешно создан'
    list_url = 'tasks:status_list'


class LabelFormCreateView(SimpleFormCreateView):
    form = LabelForm
    form_title = 'Создать метку'
    btn_title = 'Создать'
    succ_mess = 'Метка успешно создана'
    list_url = 'tasks:label_list'


class SimpleFormUpdateView(AuthRequiredMessageMixin, View):
    model = None
    form = None
    form_title = ''
    btn_title = ''
    succ_mess = ''
    list_url = ''

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=id)
        form = self.form(instance=item)
        return render(
            request,
            'tasks/create_simple.html',
            {
                'form': form,
                'form_title': self.form_title,
                'btn_title': self.btn_title
            })

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=id)
        form = self.form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(self.request, self.succ_mess)
            return redirect(self.list_url)

        return render(
            request,
            'tasks/create_simple.html',
            {
                'form': form,
                'form_title': self.form_title,
                'btn_title': self.btn_title
            })


class StatusFormUpdateView(SimpleFormUpdateView):
    model = Status
    form = StatusForm
    form_title = 'Изменение статуса'
    btn_title = 'Изменить'
    succ_mess = 'Статус успешно изменен'
    list_url = 'tasks:status_list'


class LabelFormUpdateView(SimpleFormUpdateView):
    model = Label
    form = LabelForm
    form_title = 'Изменение метки'
    btn_title = 'Изменить'
    succ_mess = 'Метка успешно изменена'
    list_url = 'tasks:label_list'


class SimpleFormDeleteView(AuthRequiredMessageMixin, View):
    model = None
    form = None
    form_title = ''
    succ_mess = ''
    err_mess = ''
    list_url = ''

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=id)
        form = self.form(instance=item)
        return render(
            request,
            'tasks/delete_simple.html',
            {
                'form': form,
                'item': item,
                'form_title': self.form_title
            })

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        item = get_object_or_404(self.model, id=id)
        if item:
            try:
                item.delete()
                messages.success(self.request, self.succ_mess)
            except ProtectedError:
                messages.error(self.request, self.err_mess)
        return redirect(self.list_url)


class StatusFormDeleteView(SimpleFormDeleteView):
    model = Status
    form = StatusFormDelete
    form_title = 'Удаление статуса'
    succ_mess = 'Статус успешно удален'
    err_mess = 'Невозможно удалить статус, потому что он используется'
    list_url = 'tasks:status_list'


class LabelFormDeleteView(SimpleFormDeleteView):
    model = Label
    form = LabelFormDelete
    form_title = 'Удаление метки'
    succ_mess = 'Метка успешно удалена'
    err_mess = 'Невозможно удалить метку, потому что она используется'
    list_url = 'tasks:label_list'



# GET /tasks/ — страница со списком всех задач
# GET /tasks/create/ — страница создания задачи
# POST /tasks/create/ — создание новой задачи
# GET /tasks/<int:pk>/update/ — страница редактирования задачи
# POST /tasks/<int:pk>/update/ — обновление задачи
# GET /tasks/<int:pk>/delete/ — страница удаления задачи
# POST /tasks/<int:pk>/delete/ — удаление задачи
# GET /tasks/<int:pk>/ — страница просмотра задачи
