from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from adminapp.forms import ShopUserCreateAdminForm, ShopUserEditAdminForm
from adminapp.utils import superuser_required
from authapp.models import ShopUser


class UserCreateView(CreateView):
    model = ShopUser
    template_name = "adminapp/user/edit.html"
    form_class = ShopUserCreateAdminForm
    success_url = reverse_lazy("admin:users")

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создание пользователя"
        return context


class UserListView(ListView):
    model = ShopUser
    template_name = "adminapp/user/users.html"
    paginate_by = 1

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Список пользователей"
        return context


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = "adminapp/user/edit.html"
    form_class = ShopUserEditAdminForm
    success_url = reverse_lazy("admin:users")

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактирование пользователя"
        return context


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = "adminapp/user/delete.html"
    success_url = reverse_lazy("admin:users")

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление пользователя"
        return context
