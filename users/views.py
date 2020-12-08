from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm(initial={"email": "hello@nico.com"})
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)

        """ #14.2 >> cleaned_data = 정리된 데이터라는 뜻으로, form.cleaned_data는 입력된 data를 dict형태로 정리해준다. """
        """ if form.isvalid()는, 입력값이 맞는지 판단하는 메소드이다. """
        """ 이때, forms에서 clean_ method를 사용하면, 받아지는 데이터를 내맘대로 바꿀수있음. """
        """     def clean_email(self):
                    print("clean email") """
        if form.is_valid():
            print(form.cleaned_data)

        return render(request, "users/login.html", {"form": form})