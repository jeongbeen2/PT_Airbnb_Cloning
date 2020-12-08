from django import forms

""" #14.1 >> form을 작성하고, 그다음 views로 넘어가서 form을 넣어준다. """


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)