from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authapp.models import ShopUser

from .forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm
from .utils import send_verify_mail


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if (
            user.activation_key == activation_key
            and not user.is_activation_key_expired()
        ):
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, "authapp/verification.html")
        else:
            print(f"error activation user: {user}")
            return render(request, "authapp/verification.html")
    except Exception as e:
        print(f"error activation user : {e.args}")
        return HttpResponseRedirect(reverse("main"))


def register(request):
    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print("сообщение подтверждения отправлено")
                return HttpResponseRedirect(reverse("auth:login"))
            else:
                print("ошибки отправки сообщения")
                return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = ShopUserRegisterForm()
    return render(
        request,
        "authapp/register.html",
        context={
            "title": "Регистрация",
            "form": register_form,
        },
    )


def login(request):
    if request.method == "POST":
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(request.user, username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if "next" in request.GET.keys():
                    return HttpResponseRedirect(request.GET["next"])
                return HttpResponseRedirect(reverse("main"))
    else:
        login_form = ShopUserLoginForm()
    return render(
        request,
        "authapp/login.html",
        context={
            "title": "Войдите в аккаунт",
            "form": login_form,
        },
    )


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


@login_required
def edit(request):
    if request.method == "POST":
        edit_form = ShopUserEditForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("main"))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    return render(
        request,
        "authapp/edit.html",
        context={
            "title": "Редактирование",
            "form": edit_form,
        },
    )


@login_required
def change_password(request):
    if request.method == "POST":
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse("main"))
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(
        request,
        "authapp/change_password.html",
        context={
            "title": "Смена пароля",
            "password_change_form": password_change_form,
        },
    )
