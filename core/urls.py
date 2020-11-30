from django.urls import path
from rooms import views as room_views


""" 여기서 만든 urlpatterns는, config>urls.py에다가 include해주어야함. """

app_name = "core"

urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]
