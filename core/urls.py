from django.urls import path
from rooms import views as room_views


""" 여기서 만든 urlpatterns는, config>urls.py에다가 include해주어야함. """

""" app_name은 urlpatterns 안의 namespace와 같아야한다. """
app_name = "core"

urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),
]
"""#11.7 >> django -> class based view는 view로 변신시켜주는 메소드가 있다. """

""" #10.3 >> all_rooms는 views.py 안에있는 def 이름과 같아야한다. """