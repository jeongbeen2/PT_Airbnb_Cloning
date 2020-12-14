from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
]
""" <str:key>가 뭔지모르겠다면, #16.4 1:30 참조. verify/뒤의 주소를 받아온다. """
""" key는, views.py에서 complete_verification 메소드의 파라메터를 의미. """