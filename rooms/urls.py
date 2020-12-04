from django.urls import path
from . import views

app_name = "rooms"

""" #12.0 >> Django Path 사용. """
""" <int:pk>를 해주면, 장고는 views.py에서 request와 pk를 받아야한다. """
""" #12.0 >> pk라는 인자는, rooms/@ -> @안의 숫자를 가져온다. """
urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]
