from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from adminapp.forms import AdminProductEditForm
from adminapp.utils import superuser_required
from mainapp.models import Product, ProductCategory


class ProductCreateView(CreateView):
    model = Product
    template_name = "adminapp/product/edit.html"
    fields = "__all__"

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            "category": self.get_category(),
        }

    def get_success_url(self):
        return reverse("adminapp:products", kwargs=self.kwargs)

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.get_category()
        return context


@superuser_required
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category).order_by("id")

    return render(
        request,
        "adminapp/product/products.html",
        context={
            "title": "Продукты",
            "category": category,
            "objects": products,
        },
    )


class ProductDetailView(DetailView):
    model = Product
    template_name = "adminapp/product/read.html"

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = AdminProductEditForm
    template_name = "adminapp/product/update.html"

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs["pk"])
        return reverse("adminapp:products", args=[product_item.category_id])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "adminapp/product/delete.html"

    def get_success_url(self):
        product_item = Product.objects.get(pk=self.kwargs["pk"])
        return reverse("adminapp:products", args=[product_item.category_id])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(
            reverse("adminapp:products", args=[self.object.category_id])
        )
