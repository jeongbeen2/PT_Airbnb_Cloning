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
from django.urls import path
from django.conf import settings

""" django에서 settings을 import할때는 위와같이 해줘야 한다. """
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
]


""" #8.4 >> settings.DEBUG == true일때만! """
""" 실제 서버가 돌아갈때는 False로, 이때는 절때 사용하지 마라. 서버가 돌아갈때마다 사진이 저장되면 """
""" 서버 줫터질꺼임 ㅎㅎ """
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)