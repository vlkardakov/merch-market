from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:id>", views.view_product, name="view_product"),
    path("payment/<int:id>", views.payment, name='payment'),
    path("success", views.success, name='success'),
    path('register/', views.register, name='register'),
    path('waiting_approval/', views.waiting_approval, name='waiting_approval'),
    path('telegram/login/', views.telegram_login, name='telegram_login'),
    path('telegram/callback/', views.telegram_callback, name='telegram_callback')

]

