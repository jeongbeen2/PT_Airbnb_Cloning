from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms
from . import models


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")
    """ #14.5 >> reverse_lazy --> url을 필요로할때만 따로 불러오는 기능. """
    """ 즉, lazy -> 바로 실행하지 않는다. """
    initial = {"email": "admin@admin.admin"}

    def form_valid(self, form):
        """ form이 유효한지 체크하는 메소드. """
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    initial = {
        "first_name": "jeong",
        "last_name": "been",
        "email": "aceman9508@gmail.com",
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


""" #16.4 >> key를 가지고온 다음, 인증하는 과정이다. """


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # to do : add success message
        # django message framework use
    except models.User.DoesNotExist:
        pass  # to do: add error message
    return redirect(reverse("core:home"))