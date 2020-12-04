from django.urls import path
from . import views

app_name = "rooms"

""" #12.0 >> Django Path 사용. """
""" <int:pk>를 해주면, 장고는 views.py에서 request와 pk를 받아야한다. """
""" #12.0 >> pk라는 인자는, rooms/@ -> @안의 숫자를 가져온다. """


urlpatterns = [path("<int:pk>", views.RoomDetail.as_view(), name="detail")]
""" #12.4 >> views.room_detail -> RoomDetail.as_view() 수정. """

""" #12.4 >> Django는, DetailView를 사용하면 자동적으로 pk라는 인자를 찾는다. """
""" 만일,<int:pk>에서 pk라는 이름을 바꾸고싶다면 ccbv가서 찾아봐라. ex.pk_url_kwarg = "potato" """