from django import forms

from authapp.forms import ShopUserEditForm, ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


class ShopUserEditAdminForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = "__all__"


class ShopUserCreateAdminForm(ShopUserRegisterForm):
    class Meta:
        model = ShopUser
        fields = (
            "username",
            "first_name",
            "email",
            "age",
            "avatar",
            "city",
            "phone",
        )


class AdminProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""


class ProductCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
