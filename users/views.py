import requests
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms
from . import models
import os


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


def github_login(request):
    client_id = os.environ.get("GH_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user"
    )


""" github docs """
""" #17.1 >> https://docs.github.com/en/free-pro-team@latest/developers/apps/authorizing-oauth-apps """


def github_callback(request):
    client_id = os.environ.get("GH_ID")
    client_secret = os.environ.get("GH_SECRET")
    code = request.GET.get("code", None)
    if code is not None:
        result = requests.post(
            f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            headers={"Accept": "application/json"},
        )
        result_json = result.json()
        error = result_json.get("error", None)
        if error is not None:
            return redirect(reverse("users:login"))
        else:
            access_token = result_json.get("access_token")
            profile_request = requests.get(
                "https://api.github.com/user",
                headers={
                    "Authorization": f"token {access_token}",
                    "Accept": "application/json",
                },
            )
            profile_json = profile_request.json()
            username = profile_json.get("login", None)
            if username is not None:
                """ github api 내에서 정보를 받아올 수 있다. """
                name = profile_json.get("name")
                email = profile_json.get("email")
                bio = profile_json.get("bio")
                user = models.User.objects.get(email=email)
                if user is not None:
                    return redirect(reverse("users:login"))
                else:
                    user = models.User.objects.create(
                        username=email, first_name=name, bio=bio, email=email
                    )
                    login(request, user)
                    return redirect(reverse("core:home"))
            else:
                return redirect(reverse("users:login"))
    else:
        return redirect(reverse("core:home"))


""" #17,2 >> access_token을 code에서 받은거로 request를 했는데, access_token은 두번 받을수 없다. """
""" {'error': 'bad_verification_code', 'error_description': 'The code passed is incorrect or expired.',
 'error_uri': 'https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-
 request-errors/#bad-verification-code'} """

""" github API에 access token 보내기 """


""" #17.2 >> 전체적인 흐름 """
""" request에서 정보를 가져오고, 정보가 없다면 None값으로 정해준다. """
""" ex> username = profile_json.get("login", None) """
""" 그다음, 상황에맞게, username이 있다면 그대로 진행하고, 만약 username이 없다면 전 페이지로 return 해준다. """
""" ex> return redirect(reverse("users:login")) """
""" redirect(reverse("")) => ""페이지로 다시 돌려보냄. """