"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

""" django에서 settings을 import할때는 위와같이 해줘야 한다. """
from django.conf.urls.static import static

""" #10.0 우리는 새로운 url을 생성할때마다 이곳으로 모조리 모이는 것을 막아야 하기 때문에, """
""" 이름에 맞는 url파일로 들어가게 해주어야 한다. ex)rooms, users 등,  """
""" 그리고 login,logout같은 것들은 core로 가게한다. """

""" urlpatterns은, urls.py에서 무조건 필수다. """
urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]


""" #8.4 >> settings.DEBUG == true일때만! """
""" 실제 서버가 돌아갈때는 False로, 이때는 절때 사용하지 마라. 서버가 돌아갈때마다 사진이 저장되면 """
""" 서버 줫터질꺼임 ㅎㅎ """
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)