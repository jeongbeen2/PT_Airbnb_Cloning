from django.urls import path
from rooms import views as room_views


""" 여기서 만든 urlpatterns는, config>urls.py에다가 include해주어야함. """

""" app_name은 urlpatterns 안의 namespace와 같아야한다. """
app_name = "core"

urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]
""" #10.3 >> all_rooms는 views.py 안에있는 def 이름과 같아야한다. """