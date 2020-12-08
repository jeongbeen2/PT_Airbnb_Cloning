from django import forms
from . import models

""" #14.1 >> form을 작성하고, 그다음 views로 넘어가서 form을 넣어준다. """


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    """ #14.2 >> 이메일이나, 비밀번호가 있는 field를 확인하고 싶으면 clean_ 을 붙여야한다. """

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)  # email이 실제 유저의 이메일과 같은지 체크
            if user.check_password(password):  # password 유효한지 체크
                return self.cleaned_data
                # clean을 사용했다면, 항상 return값은 cleaned_data로 해주어야한다.
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("USer does not exist"))

    """ #14.3 >> def clean으로 할거면, 에러가 뜨는곳을 직접 add_error 해줘서 넣어주어야 하고, """
    """ def clean_email, password처럼 각각 해줄꺼면 raise password, email 해주면 그자리에 뜬다. """