from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "hello@nico.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


""" #14.5 >> LoginView에 대해 더 자세히 알고싶다면 """
""" https://docs.djangoproject.com/en/2.2/topics/auth/default/ """

""" FormView는, form에서 인증하고싶을때 좋다. """
""" ccbv에서 확인. """

""" reverse는, core:home으로 가서 실제 url을 가져다준다. """