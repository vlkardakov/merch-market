from django.contrib import admin
from .models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    pass

class ReviewAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)