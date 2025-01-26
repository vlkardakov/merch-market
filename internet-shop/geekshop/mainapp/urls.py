from django.urls import path

from . import views

app_name = "mainapp"

urlpatterns = [
    path("", views.products, name="all"),
    path("<int:category_id>", views.category, name="category"),
    path("<int:category_id>/<int:page>", views.category, name="paged_category"),
    path("product/<int:product_id>", views.product, name="product"),
]
